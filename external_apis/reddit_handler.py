import praw
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client_id = os.environ.get('REDDIT_PUBLIC_KEY')
client_secret = os.environ.get('REDDIT_PUBLIC_SECRET')
username = os.environ.get('REDDIT_USERNAME')
password = os.environ.get('REDDIT_PASSWORD')

def get_subreddit_content(subreddit_name, error_msg):
    try:
        reddit_inst = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            password=password,
                            user_agent='contentscript by /u/pimpdaddyballer',
                            username=username)

        puppies_subreddit = reddit_inst.subreddit(subreddit_name)

        return puppies_subreddit.random().url

    except praw.exceptions.ClientException as e:
        print(e)
        return None
    except praw.exceptions as e:
        print(e)
        return error_msg

def random_puppy():
    out = None
    while out == None:
        out = get_subreddit_content('puppies', "I choked on cuteness, try again!")
    return out

def random_kitten():
    out = None
    while out == None:
        out = get_subreddit_content('kittens', "I choked on cuteness, try again!")
    return out

def random_cute():
    out = None
    while out == None:
        out = get_subreddit_content('aww', "I choked on cuteness, try again!")
    return out

if __name__ == '__main__':
  random_puppy()
