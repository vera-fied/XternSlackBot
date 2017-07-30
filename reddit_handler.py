import praw

def get_subreddit_content(subreddit_name, error_msg):
    with open(".env") as f:
        content = f.readlines()

    client_id = (content[4].split("="))[1].strip('\n')
    client_secret = (content[5].split("="))[1].strip('\n')
    username = (content[6].split("="))[1].strip('\n')
    password = (content[7].split("="))[1].strip('\n')

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
