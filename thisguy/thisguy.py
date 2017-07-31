def addReactions(slack_client, channel, ts):
    slack_client.api_call('reactions.add', ':scrabble-f:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-u:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-c:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-k:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-blank:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-a:', channel, ts)
    slack_client.api_call('reactions.add', ':scrabble-j:', channel, ts)

admin = os.environ.get('ADMIN_USER')

def handle_message(slack_client, command, channel, user):
    res = command.split(' ')
    if(user == admin and command[1] == ":scrabble-f::scrabble-u::scrabble-c::scrabble-k::scrabble-blank::scrabble-a::scrabble-j:"):
        os.environ['ADD_REACTIONS'] = command[2]
