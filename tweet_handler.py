import tweepy
import random

def trump_tweet():
    with open(".env") as f:
        content = f.readlines()

    consumer_key = (content[0].split("="))[1].strip('\n')
    consumer_secret = (content[1].split("="))[1].strip('\n')
    token_key = (content[2].split("="))[1].strip('\n')
    token_secret = (content[3].split("="))[1].strip('\n')
    
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
