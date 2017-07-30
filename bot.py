import os
import time
import json
from slackclient import SlackClient
from scrabble import scrabblify;


BOT_ID = os.environ.get("BOT_ID")

AT_BOT = "<@" + BOT_ID + ">"
adminid = os.environ.get('ADMIN_TOKEN')

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))
if(adminid):
    admin = SlackClient(adminid)

def handle_command(command, channel, senduser, ts):
    if(command.startswith("scrabblify")):
        inputStr = command[11:]
        output = scrabblify(inputStr, False)
        users = slack_client.api_call('users.list')
        users = users.get("members")
        for user in users:
            if('id' in user and user.get('id') == senduser):
                print(user)
                name = user['name']
                url = user.get("profile").get('image_original')
        if(adminid):
            admin.api_call("chat.delete", channel=channel, ts=ts, as_user=True, token=adminid)
        else:
            print("Cannot delete message, not an admin")
        slack_client.api_call("chat.postMessage", channel=channel, text=output, as_user=False, username=name, icon_url=url)
        

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return (output['text'].split(AT_BOT)[1].strip().lower(), output['channel'], output['user'], output['ts'])
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            stuff = parse_slack_output(slack_client.rtm_read())
            if stuff[0] and stuff[1] and stuff[2]:
                print(stuff[0])
                print(stuff[1])
                print(stuff[2])
                print(stuff[3])
                handle_command(stuff[0], stuff[1], stuff[2], stuff[3])
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
