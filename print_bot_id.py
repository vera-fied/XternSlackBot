"""TEST FOR BOT"""
import os

from slackclient import SlackClient

BOT_NAME = 'urmumxxx123'

slack_token = os.environ["SLACK_API_TOKEN"]
slack_client = SlackClient(slack_token)


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
