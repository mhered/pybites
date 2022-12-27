import os
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from pprint import pprint 

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path(os.getenv("TMP", "/tmp"))
html_file = tmp / "books.html"


if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instantiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title:str, author:str, year:int, rank: int, rating:float):
        self.title = title # as it appears on the page
        self.author = author # should be entered as lastname, firstname
        self.year = year # four digit integer year that the book was published
        self.rank = rank # integer rank to be updated once the books have been sorted
        self.rating = float(rating) # float as indicated on the page


    def __repr__(self):
        return f'[{self.rank:03d}] {self.title} ({self.year})\n      {self.author} {self.rating}'

def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    books_until_year = [book for book in books if year and book.year >= year]
    for book in books_until_year[:limit]:
        print(book)


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    books = soup.find_all('div', {'class': 'book accepted normal'})
    result = []
    for book in books:
        try:
            rank = book.find('div', {'class': 'rank'}).span.get_text()
            title = book.find('h2', {'class':  'main'}).get_text()
            authors = book.find('h3', {'class':  'authors'}).a.get_text()
            year = book.find('span', {'class': 'date'}).get_text().strip('| ')
            rating = book.find('span', {'class':  'our-rating'}).get_text()
        except AttributeError:
            continue
        # format
        rank = int(rank)
        # assumes one author only and surname is last word only
        names = authors.split()
        name= " ".join(names[:-1]) 
        surname = names[-1]
        author = f'{surname}, {name}'
        year = int(year) # why insists in 4 digits?
        rating = float(rating)
        if 'python' in title.lower():
            result.append(Book(title, author, year, rank, rating))
    # sort descending by rating 
    # ascending by year, 
    # by title case insensitive but don't change the original
    # and then by author's last name
    # in that order
    result.sort(key=lambda x:x.author.split(',')[0])
    result.sort(key=lambda x:x.title.lower())
    result.sort(key=lambda x:x.year)
    result.sort(key=lambda x:x.rating, reverse = True)
    # update ranks
    for i, book in enumerate(result):
        book.rank = i+1
    return result
        


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""