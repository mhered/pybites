from collections import namedtuple
from datetime import date

import feedparser
import re
from pprint import pprint

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    year, month, day, *_ = stime
    return date(year=year,month=month,day=day)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    feed = feedparser.parse(feed)
    lst = []
    for entry in feed.entries:
        
        entry_tags = [tag['term'].lower() for tag in entry.tags]
        # print(entry_date, entry.title, entry.link, entry_tags)
        lst.append(Entry(_convert_struct_time_to_dt(entry.published_parsed), entry.title, entry.link, entry_tags))
    return lst

def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if '&' in search:
        words = search.split('&')
        return all(filter_entries_by_tag(word,entry) for word in words)
    elif '|' in search:
        words = search.split('|')
        return any(filter_entries_by_tag(word,entry) for word in words)
    else:
        return any(search.lower() == tag.lower() for tag in entry.tags)
        

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    
    entries  = get_feed_entries()
    
    while True:
    
        usr_input = input('Search for (q for exit):')
    
        if not usr_input:
            print('Please provide a search term')
            continue

        if usr_input.lower() =='q':
            print('Bye')
            break
        else:
            filtered_entries = [entry for entry in entries if filter_entries_by_tag(usr_input, entry)]
            if filtered_entries:
                for entry in  sorted(filtered_entries, key=lambda x:x.date):
                    print(f'{entry.date} | {entry.title:<42} | {entry.link}')

            entrx = 'entry' if len(filtered_entries)==1 else 'entries'

            print(f'\n\t{len(filtered_entries)} {entrx} matched "{usr_input}"\n')
                

if __name__ == '__main__':
    main()