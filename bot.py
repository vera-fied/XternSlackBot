import os
import time
import json
from slackclient import SlackClient

import tweet_handler
import reddit_handler

BOT_ID = "U6FGNSVHA"

AT_BOT = "<@" + BOT_ID + ">"

slack_client = SlackClient("xoxb-219566913588-zZH2pR0BkLh0quDK3EJwEHGB")

def handle_command(command, channel, user):
    if(command=="test"):
        slack_client.api_call("chat.postMessage", channel=channel, text="tested", as_user=True)
    elif(command=="!trump"):
        to_post = tweet_handler.trump_tweet()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True)
    elif(command=="!puppy"):
        to_post = reddit_handler.random_puppy()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
    elif(command=="!kitten"):
        to_post = reddit_handler.random_kitten()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
    elif(command=="!cute"):
        to_post = reddit_handler.random_cute()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)

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
                return (output['text'].split(AT_BOT)[1].strip().lower(), output['channel'], output['user'])
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            read_output = slack_client.rtm_read()
            stuff = parse_slack_output(read_output)
            if stuff[0] and stuff[1] and stuff[2]:
                print(stuff[0])
                print(stuff[1])
                print(stuff[2])
                handle_command(stuff[0], stuff[1], stuff[2])
            # time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
