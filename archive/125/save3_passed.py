from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()

    soup = BeautifulSoup(content, 'html.parser')
    entry = soup.find("div", class_="entry-content")
    links = entry.find_all("a")
    result = []
    for link in links:
        # get text in the span/em inside a if href contains AMAZON
        if AMAZON in link.get("href"): 
            book_title = link.find({"span","em"}).text.strip()
            result.append(book_title)
    count_books = Counter(result)
    return sorted([ (title, count) for title, count in count_books.items() if count >= MIN_COUNT ] , \
            key=lambda tup: tup[1], reverse=True)

print(get_top_books())