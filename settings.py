import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1200

# The maximum rent you want to pay per month.
MAX_PRICE = 2700

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'fortcollins'

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "old-town": [
        [-105.089157,40.577464],
        [-105.056927,40.593076]
    ],
    "north-prospect": [
        [-105.077909,40.566391],
        [-105.042559,40.578611]
    ],
    "north-drake": [
        [-105.079375,40.550778],
        [-105.018972,40.568308]
    ]
    # "wicker-park": [
    #     [-87.68815,41.902788], # bottom-left, reversed lat-long
    #     [-87.666864,41.925398] # top-right, reversed lat-long
    # ],
    # "chicago": [
    #     [-87.95517,41.640078],
    #     [-87.511597,42.026854]
    # ]
}


## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 30 * 60 # 30 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#starship_database"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
