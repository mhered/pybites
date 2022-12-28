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
    title = [element.find("h2").text.strip() for element in dotd_title_div][0]
    
    dotd_description_parent_div = soup.find('div', class_="dotd-main-book-summary")
    description = list(dotd_description_parent_div.children)[7]
    description = description.text.strip()

    dotd_link_div = soup.find_all('div', class_="dotd-main-book-image")
    for element in dotd_link_div:
        link = element.find("a")
    link = link["href"]

    dotd_image_img = soup.find('img', class_="imagecache-dotd_main_image")
    image = dotd_image_img["src"]
    
    book = Book(title, description, image, link)
    return book


if __name__ == "__main__":
    print(get_book())