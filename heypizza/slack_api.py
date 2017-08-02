def send_message(channel, message, slack):
	if slack is None:
		return

	slack.api_call(
		'chat.postMessage',
		channel=channel,
		text=message
	)


def get_user(user_id, members):
	for member in members:
		if member['id'].lower() == user_id.lower():
			return member
	return {
		'name': ''
	}


def convert_to_tag(username, members):
	for member in members:
		if member['name'] == username:
			return '<@' + member['id'] + '|' + username + '>'
	return '@' + username
