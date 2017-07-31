import os

def addReactions(slack_client, channel, ts):
    slack_client.api_call('reactions.add', name='scrabble-f', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-u', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-c', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-k', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-blank', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-a', channel=channel, timestamp=ts)
    slack_client.api_call('reactions.add', name='scrabble-j', channel=channel, timestamp=ts)

admin = os.environ.get('ADMIN_USER')

def handle_message(slack_client, command, channel, user):
    res = command.split(' ')
    if(user == admin and res[0] == ":scrabble-f::scrabble-u::scrabble-c::scrabble-k::scrabble-blank::scrabble-a::scrabble-j:"):
        os.environ['ADD_REACTIONS'] = res[1].lower()
        print("Set add reactions to: " + res[1])
        return ""
    else:
        return None
