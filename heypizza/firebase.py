from dotenv import load_dotenv, find_dotenv
import pyrebase
import os

load_dotenv(find_dotenv())
config = {
	'apiKey': os.environ.get('SLACK_API_TOKEN'),
	'authDomain': 'xtern-slack-bot.firebaseapp.com',
	'databaseURL': 'https://xtern-slack-bot.firebaseio.com/',
	'storageBucket': 'xtern-slack-bot.appspot.com'
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


def db_get(long_key, prop):
	res = db.child('users/' + long_key).get().val()
	if res is None:
		return None
	elif prop is None:
		return res
	else:
		try:
			return res[prop]
		except KeyError:
			return None


def db_set(long_key, value):
	db.child('users/' + long_key).update(value)