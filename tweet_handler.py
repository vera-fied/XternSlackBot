from TwitterSearch import *

def trump_tweet():
    with open("secrets.txt") as f:
        content = f.readlines()

    if len(content) != 4:
        print("Invalid auth file")
        return None

    con_key = (content[0].split("="))[1].strip('\n')
    con_secret = (content[1].split("="))[1].strip('\n')
    token_key = (content[2].split("="))[1].strip('\n')
    token_secret = (content[3].split("="))[1].strip('\n')

    try:
        tuo = TwitterUserOrder('realDonaldTrump')

        ts = TwitterSearch(
            consumer_key = con_key,
            consumer_secret = con_secret,
            access_token = token_key,
            access_token_secret = token_secret,
        )
        
        for tweet in ts.search_tweets_iterable(tuo):
            output = '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] )
            return output

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

def ():
    with open("secrets.txt") as f:
        content = f.readlines()

    if len(content) != 4:
        print("Invalid auth file")
        return None

    con_key = (content[0].split("="))[1].strip('\n')
    con_secret = (content[1].split("="))[1].strip('\n')
    token_key = (content[2].split("="))[1].strip('\n')
    token_secret = (content[3].split("="))[1].strip('\n')

    try:
        tuo = TwitterUserOrder('realDonaldTrump')
        tuo.set_include_entities(True)
        tso.set_include_entitie

        ts = TwitterSearch(
            consumer_key = con_key,
            consumer_secret = con_secret,
            access_token = token_key,
            access_token_secret = token_secret,
        )
        
        for tweet in ts.search_tweets_iterable(tuo):
            output = '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] )
            return output

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

if __name__ == '__main__':
  print(trump_tweet())
