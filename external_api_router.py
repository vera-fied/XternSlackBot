import os
from slackclient import SlackClient

import tweet_handler
import reddit_handler 

slack_client = SlackClient(os.environ.get('SLACK_API_TOKEN'))

def handle_message(command, channel, user):
    if(command=="!trump"):
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