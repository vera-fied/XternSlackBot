from dotenv import load_dotenv, find_dotenv
from datetime import date
from .firebase import db_get, db_set
from .slack_api import send_message, get_user, __init__
from .string_util import parse_message, make_error_message, make_message, leaderboards

load_dotenv(find_dotenv())


def handle_message(slack_client, message, channel, user):
	if 'leaderboard' in message:
		send_message(channel, leaderboards(), slack_client)
		return ""

	if ':pizza:' not in message:
		return None

	members = slack_client.api_call('users.list')['members']
	pizzas = parse_message(message, members)
	user_name = get_user(user, members)['name']

	if verify_pizzas(pizzas, user_name):
		save_pizzas(pizzas, user_name)
		text = make_message(pizzas, user_name, members)
	else:
		text = make_error_message(pizzas, user_name)

	send_message(channel, text, slack_client)
	return ""


def verify_pizzas(pizzas, user):
	num_pizzas = pizzas['numPizzas'] * len(pizzas['users'])

	sent_pizzas = db_get(user, 'given')
	last_day_given = db_get(user, 'lastDayGiven')
	if last_day_given is not None and (date.today() - date.fromordinal(last_day_given)).days > 0 or sent_pizzas is None:
		sent_pizzas = 0

	return sent_pizzas + num_pizzas <= 5


def save_pizzas(pizzas, user):
	old_given = db_get(user, 'given')
	if old_given is None:
		old_given = '0'
	db_set(user, {
		'lastDayGiven': date.today().toordinal(),
		'given': int(old_given) + pizzas['numPizzas']
	})

	for p_user in pizzas['users']:
		old_given = db_get(p_user, 'received')
		if old_given is None:
			old_given = '0'
		db_set(p_user, {
			'received': int(old_given) + pizzas['numPizzas']
		})
