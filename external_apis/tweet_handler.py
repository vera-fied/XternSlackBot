import random
import os
import tweepy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
token_key = os.environ.get('TWITTER_TOKEN_KEY')
token_secret = os.environ.get('TWITTER_TOKEN_SECRET')

def trump_tweet():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(token_key, token_secret)

        api = tweepy.API(auth)
        tweets = api.user_timeline(id='realDonaldTrump', count=1)
        for tweet in tweets:
            output = '@%s tweeted: %s' % ( tweet.user.screen_name, tweet.text)
            return output

    except tweepy.TweepError as e:
        print(e)

if __name__ == '__main__':
  trump_tweet()
