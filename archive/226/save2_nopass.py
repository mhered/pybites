from collections import namedtuple

from bs4 import BeautifulSoup
import requests
import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    # your code ...
    lst=[]
    
    titles_spans=soup.find_all('span',{'class':'title'})
    websites_spans=soup.find_all('span',{'class':'smaller'})
    points_spans=soup.find_all('span',{'class':'controls'})
    comments_spans=soup.find_all('span',{'class':'naturaltime'})
    # print(titles_spans,websites_spans,points_spans,comments_spans)

    for title,website,points,comments in zip(titles_spans,websites_spans,points_spans,comments_spans):
        title=f"{title.a.text} ({website.a.text})"
        points=int(re.search('[0-9]+',points.span.text)[0])
        comments=int(re.search('[0-9]+',comments.span.a.text)[0])
        entry=Entry(title,points,comments)
        # print(entry)
        lst.append(entry)
        
    return sorted(lst,key=lambda x:x.points+x.comments, reverse=True)[:top]
    
    
url = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'
print(get_top_titles(url))