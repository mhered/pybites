from pprint import pprint
from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.parse(FEED_URL)
    lst = []
    for entry in feed.entries:
        lst.append(Game(entry.title.encode('utf-8'), entry.link.encode('utf-8')))
            
    pprint(lst)
    return lst
    
if __name__=="__main__":
    get_games()