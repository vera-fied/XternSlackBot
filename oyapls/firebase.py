from dotenv import load_dotenv, find_dotenv
import pyrebase
import os

load_dotenv(find_dotenv())
config = {
	'apiKey': os.environ.get('SLACK_API_TOKEN'),
	'authDomain': os.environ.get('OYA_AUTH'),
	'databaseURL': os.environ.get('OYA_URL'),
	'storageBucket': os.environ.get('OYA_BUCKET'),
    'apiKey':os.environ.get('OYA_KEY'),
    'projectId':os.environ.get('OYA_PROJECT')
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
