import os
import time
import json
from slackclient import SlackClient
from .scrabble import scrabblify


def handle_command(command, channel, senduser, ts, slack_client, admin_client, adminid):
    if(command.startswith("scrabblify")):
        inputStr = command[11:]
        output = scrabblify(inputStr, False)
        users = slack_client.api_call('users.list')
        users = users.get("members")
        for user in users:
            if('id' in user and user.get('id') == senduser):
                name = user['name']
                url = user.get("profile").get('image_original')
        if(admin_client):
            admin_client.api_call("chat.delete", channel=channel, ts=ts, as_user=True, token=adminid)
        else:
            print("Cannot delete message, not an admin")
        slack_client.api_call("chat.postMessage", channel=channel, text=output, as_user=False, username=name, icon_url=url)
        return ""
    else:
        return None

