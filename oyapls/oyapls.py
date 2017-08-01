from .firebase import db_get, db_set
from random import randint
import datetime as dt
from .string_util import get_user, user_from_at
import os

oyalimit = os.environ.get('OYA_LIMIT')

def handle_message(slack_client, message, channel, user):
    if "oyapls" in message:
        oya = random_oya()
        give_oya(oya, user, slack_client, channel)
        return ""
    elif "oyas" in message:
        at_user = message.split(' ')[0]
        check_user = user_from_at(at_user).upper()
        name = get_user(check_user, slack_client).get('name')

        vals = db_get(check_user, None)
        temp = 0
        if 'oya' in vals.keys():
            temp = vals['oya']
        response = name.title() + " has " + str(temp) + " :oya:"

        for x in range(1,11):
            temp = 0
            if ('oya'+str(x)) in vals.keys():
                temp = vals['oya'+str(x)]
            response += ", " + str(temp) + " :oya" + str(x) + ":"

        temp = 0
        if 'oya-rainbow' in vals.keys():
            temp = vals['oya-rainbow']
        response += ", " + str(temp) + " :oya-rainbow:"

        temp = 0
        if 'oya-rainbow-aussie' in vals.keys():
            temp = vals['oya-rainbow-aussie']
        response += ", " + str(temp) + " :oya-rainbow-aussie:"

        temp = 0
        if 'nsfw_oya' in vals.keys():
            temp = vals['nsfw_oya']
        response += ", and " + str(temp) + " :nsfw_oya:."

        slack_client.api_call('chat.postMessage', channel=channel, text = response, as_user=True)
        return ""
    elif (":oya" in message or ":nsfw_oya:" in message):
        inputs = message.split(' ')
        length = len(inputs)
        at_user = inputs[0]
        check_user = user_from_at(at_user).upper()
        name = get_user(check_user, slack_client).get('name')
        vals = db_get(user, None)
        add_vals = db_get(check_user, None)
        response = ""

        i = 1
        while(i < length):
            if inputs[i].isnumeric():
                num = int(inputs[i])
                i+=1
                if "oya" in inputs[i]:
                    oya = inputs[i]
                    oya = oya[1:-1]
                    if (oya in vals and vals[oya] >= num):
                        db_set(user, {oya:vals[oya] - num})
                        if (add_vals != None and oya in add_vals):
                            db_set(check_user, {oya:add_vals[oya]+num})
                        else:
                            db_set(check_user, {oya:num})
                        response+="Gave " + str(num) + " :" + oya + ": to " + name +". "
                        i+=1
                    else:
                        slack_client.api_call('chat.postMessage', channel=channel, text = "Not enough :"+oya+": to give.", as_user=True)
                        return ""
                else:
                    slack_client.api_call('chat.postMessage', channel=channel, text = "No oya provided for a number.", as_user=True)
                    return ""
            else:
                slack_client.api_call('chat.postMessage', channel=channel, text = "Out of order arguments", as_user=True)
                return ""
        slack_client.api_call('chat.postMessage', channel=channel, text = response, as_user=True)
        return ""
    else:
        return None


def give_oya(oya, user, slack_client, channel):
    vals = db_get(user, None)
    name = get_user(user, slack_client).get('name')

    oyas_left = None
    if (vals != None and 'daily_oyas' in vals.keys()):
        oyas_left = vals['daily_oyas']
    last_day = None
    if (vals != None and 'last_day' in vals.keys()):
        last_day = vals['last_day']
    last_hour = None
    if (vals != None and 'last_hour' in vals.keys()):
        last_hour = vals['last_hour']

    if (last_day is None or last_hour is None or ((dt.date.today().toordinal() - last_day) * 24 + dt.datetime.now().hour - last_hour > 0 or oyas_left is None)):
        oyas_left = int(oyalimit)
    if oyas_left == 0:
        slack_client.api_call('chat.postMessage', channel=channel, text = name.title() + " has already gotten 2 oyas this hour.", as_user=True)
        return

    if (vals != None and oya in vals.keys()):
        old_oyas = vals[oya] 
    else:
        old_oyas = 0
    db_set(user, {
        oya: old_oyas+1,
        'last_day': dt.date.today().toordinal(),
        'last_hour': dt.datetime.now().hour,
        'daily_oyas': oyas_left - 1
    })
    slack_client.api_call('chat.postMessage', channel=channel, text = name.title() + " got a :" + oya + ":.", as_user=True)

def random_oya():
    rand = randint(1,32767)
    power = 14
    count = 2 ** power
    while (rand > count):
        power-=1
        count += 2 ** power
    power = 14 - power
    if power == 0:
        return "oya"
    elif power == 12:
        return "oya-rainbow"
    elif power == 13:
        return "oya-rainbow-aussie"
    elif power == 14:
        return "nsfw_oya"
    else:
        return "oya" + str(power)


