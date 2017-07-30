import os
from slackclient import SlackClient

from .tweet_handler import *
from .reddit_handler import *

def handle_message(command, channel, user, slack_client):
    if(command=="!trump"):
        to_post = trump_tweet()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True)
        return ""
    elif(command=="!puppy"):
        to_post = random_puppy()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
        return ""
    elif(command=="!kitten"):
        to_post = random_kitten()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
        return ""
    elif(command=="!cute"):
        to_post = random_cute()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
        return ""
    elif(command=="!love"):
        to_post = random_sfw()
        slack_client.api_call("chat.postMessage", channel=channel, text=to_post, as_user=True, unfurl_media=True)
        return ""
    else:
        return None