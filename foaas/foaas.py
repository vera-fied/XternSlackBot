import requests
import ssl

def handle_command(command, channel, user, slack_client, admin, ts):
    if(command.split(' ')[0].lower() == 'foaas'):
        processFoaas(command, channel, user, slack_client, admin, ts)
        return ""
    else:
        return None

def processFoaas(command, channel, user, slack_client, admin, ts):
    payload = {'Accept': 'text/plain'}
    pieces = command.split(' ')[1:]

    if(pieces[0] == 'help'):
        r = requests.get("https://www.foaas.com/operations")
        text = "Use any of the following commands, with spaces delimiting instead of slashes. Do not use :from, it will default as your name. If you do not give it a valid value, it will return a generic response.\n"
        json = r.json()
        for i in json:
            text += i['url'] + "\n"
        slack_client.api_call('chat.postMessage', channel=channel, text = text, as_user=True)
        return ""

    tohit = ""
    for word in pieces:
        tohit += "/" + word

    if(tohit == ""):
        slack_client.api_call('chat.postMessage', channel=channel, text = "You didn't give a request for foaas", as_user=True)
        return ""

    name = ""
    members = slack_client.api_call('users.list')['members']
    for member in members:
        if member['id'].lower() == user.lower():
            name = member['profile']['first_name'].title()

    r = requests.get("https://www.foaas.com" + tohit + "/" + name, headers=payload)

    if(r.status_code == 622):
        slack_client.api_call('chat.postMessage', channel=channel, text = "Invalid foaas request.", as_user=True)
    elif(r.status_code == requests.codes.ok):
        if(admin):
            admin.api_call("chat.delete", channel=channel, ts=ts, as_user=True)
        else:
            print("Cannot delete message, not an admin")
        slack_client.api_call('chat.postMessage', channel=channel, text = r.text, as_user=True)
    else:
        slack_client.api_call('chat.postMessage', channel=channel, text = "Error retrieving from foaas. Status code: " + r.status_code, as_user=True)

    return ""
