# XternSlackBot
Slackbot made for use in the Xtern slack


To use, copy conf-ex.py to conf.py and edit the values.

## Dependencies
    pip install slackclient
    pip install python-dtenv
    pip install pyrebase
    pip install praw
    pip install tweepy

First change the BOT_NAME in print_bot_id.py to whatever your bot name is. Set the slack_token with `export SLACK_API_TOKEN="yourslacktoken"`. Run print_bot_id.py and then `export BOT_ID="outputOfPrintID"`.

Get a legacy token from an admin account at `https://api.slack.com/custom-integrations/legacy-tokens` and put it into ADMIN_TOKEN `export ADMIN_TOKEN="yourAdminToken"`

Then run bot.py to start the bot
