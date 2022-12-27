import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    date_str_clean = re.findall(',(.+)\+',date_str)[0]
    return datetime.strptime(date_str_clean.strip(), "%d %B %Y %H:%M:%S")


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    return collections.Counter([date.strftime("%Y-%m") for date in dates]).most_common(1)[0][0]


if __name__=="__main__":
    test_str="Thu, 04 May 2017 20:46:00 +0200."
    test_lst =[
        datetime(year=2021, month=10, day=1),
        datetime(year=2022, month=10, day=10),
        datetime(year=2023, month=10, day=11),
        datetime(year=2021, month=11, day=12),
        datetime(year=2022, month=10, day=2),
        datetime(year=2022, month=10, day=3),
        datetime(year=2021, month=9, day=6)
        ]
    
    date = convert_to_datetime(test_str)
    print(date.strftime("%Y-%d"))
    print(get_month_most_posts(test_lst))
