from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    dotd_title_div = soup.find_all('div', class_="dotd-title")
    
    """ this works
    for element in dotd_title_div:
        title_element = element.find("h2")
    return title_element.text.strip()
    """
    
    return [element.find("h2").text.strip() for element in dotd_title_div][0]


if __name__ == "__main__":
    print(get_book())