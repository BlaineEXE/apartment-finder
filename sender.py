from slackclient import SlackClient
#import private
import settings

#SLACK_TOKEN = private.SLACK_TOKEN
settings.SLACK_TOKEN
SLACK_CHANNEL = "#starship_database"

sc = SlackClient(settings.SLACK_TOKEN)

def post_to_slack(listing, neighborhood):
    desc = "{} | {} | <{}> ".format(str(neighborhood), listing["name"], listing["url"])
    sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
        username='Craigslist Apartment Bot', icon_emoji=':house:'
    )
