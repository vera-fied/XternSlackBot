members = []
slack = None


def __init__(slack_client):
	global members, slack
	slack = slack_client
	members = slack_client.api_call('users.list')['members']


def send_message(channel, message):
	if slack is None:
		return

	slack.api_call(
		'chat.postMessage',
		channel=channel,
		text=message
	)


def get_user(user_id):
	for member in members:
		if member['id'].lower() == user_id.lower():
			return member
	return {
		'name': ''
	}


def convert_to_tag(username):
	for member in members:
		if member['name'] == username:
			return '<@' + member['id'] + '|' + username + '>'
	return '@' + username
