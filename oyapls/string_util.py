def get_user(user_id, slack_client):
    members = slack_client.api_call('users.list')['members']
    for member in members:
        if member['id'].lower() == user_id.lower():
            return member
    return ""

def user_from_at(user):
    if user[1] == '@':
        return user[2:-1]
    else:
        return None
