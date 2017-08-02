from .slack_api import convert_to_tag, get_user
from .firebase import db_get


def parse_message(message, members):
	return {
		'numPizzas': message.count(':pizza:'),
		'users': [get_user(word[2:-1], members)['name'] for word in message.split(' ') if '@' in word]
	}


def make_message(pizzas, user, members):
	val = (
		convert_to_tag(user, members) + ' sent ' + str(pizzas['numPizzas']) + ' pizzas to ' +
		convert_to_tag(pizzas['users'][0], members)
	)
	if len(pizzas['users']) > 1:
		val += (
			', ' + [convert_to_tag(user, members) for user in pizzas['users'][1:-1]].join(', ') + ', and ' +
			convert_to_tag(pizzas['users'][-1], members)
		)
	return val


def make_error_message(pizzas, user):
	old_num = db_get(user, 'given')
	if old_num is None:
		old_num = 0
	else:
		old_num = int(old_num)

	return (
		'Oops! You can only send 5 pizzas per day. @' + user + ' already sent ' + str(old_num) + ' pizzas earlier ' +
		'today, and they tried to send another ' + str(pizzas['numPizzas']) + '. Wait until tomorrow for another 5!'
	)


def leaderboards():
	root = db_get('', None)
	users = reversed(sorted(root, key=lambda x: get_received(root, x)))
	scores = '*LEADERBOARD*'
	i = 1
	for user in users:
		scores += '\n' + str(i) + ') @' + user + ' (with ' + str(get_received(root, user)) + ' pizzas)'
		i += 1
	return scores


def get_received(root, x):
	try:
		return root[x]['received']
	except KeyError:
		return 0
