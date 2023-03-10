from abc import ABC, abstractmethod
from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from os import getenv, path
from pathlib import Path
from typing import Any, List, Optional, NamedTuple
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup  # type: ignore

TMP = getenv("TMP", "/tmp")
TODAY = date.today()

Candidate = NamedTuple("Candidate", [
        ('name', str), 
        ('votes', int),
    ]
)
LeaderBoard = NamedTuple(
    "LeaderBoard", [
        ('Candidate', str), 
        ('Average', str), 
        ('Delegates', str), 
        ('Contributions', str), 
        ('Coverage', str),
    ]
)
Poll = NamedTuple(
    "Poll",[
        ('Poll', str),
        ('Date', str),
        ('Sample', int),
        ('Sanders', float),
        ('Biden', float),
        ('Gabbard', float),
        ('Spread', float),
    ]
)


def as_float(string):
    try:
        return float(string)
    except ValueError:
        return 0        

@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """
    name: str
    path: Path = ''
    
    def __post_init__(self):
        if self.path:
            self.path = Path(self_path , self.name)
        else:
            self.path = Path(TMP,f'{TODAY}_{self.name}')
        
    @property
    def data(self) -> Optional[str]:
        if path.isfile(self.path):
            with open(self.path) as f:
                return f.read()
        else:
            return None

@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """
    url: str
    file: File

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if not self.file.data:
            urlretrieve(self.url, self.file.path)
        return self.file.data

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        soup = Soup(self.data, 'html.parser')
        return soup


class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should be implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """
    web: Web

    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
            
        return self.web.soup.find_all('table')[loc or 0]

    @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]:
        """Abstract Method
        
        Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def polls(self, table: int = 0) -> List[Any]:
        """Abstract Method

        Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass
    
    @abstractmethod
    def stats(self, loc: int = 0):
        """Abstract Method
        
        Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    web:Web

    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        lst=[]
        for row in table.find_all('tr')[2:]:
            tds=row.find_all('td')
            poll=tds[0].text
            date=tds[1].text
            sample=as_float(tds[2].text)
            biden=as_float(tds[3].text)
            sanders=as_float(tds[4].text)
            gabbard=as_float(tds[5].text)
            spread=as_float(tds[5].text)
            lst.append(Poll(poll, date, sample, sanders, biden, gabbard, spread))
        # print(lst)
        return lst

    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        return self.parse_rows(self.find_table(table))

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        output="""\nRealClearPolitics\n=================\n"""
        for candidate in 'Biden', 'Sanders', 'Gabbard':
            output+=f'{candidate:>9}: {sum(getattr(poll, candidate) for poll in self.polls(loc))}\n'
        print(output)


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        lst=[]
        for row in table.find_all('tr')[1:4]:
            tds=row.find_all('td')
            candidate=tds[0].text.strip()
            average=tds[1].text.strip()
            delegates=int(tds[2].text.strip())
            contributions=tds[3].text.strip()
            coverage=int(tds[4].text.strip('# '))
            # print(" # ".join([candidate, average, delegates, contributions, coverage]))
            lst.append(LeaderBoard(candidate, average, delegates, contributions, coverage))
        # print(lst)
        return lst
        

    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        return self.parse_rows(self.find_table(table))

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        output=f"\nNYTimes\n{'='*33}\n\n"
        for item in self.polls(loc):
            output+=f"{item.Candidate:>33}\n{'-'*33}\n"
            output+=f'{"National Polling Average":>24}: {item.Average}\n'
            output+=f'{"Pledged Delegates":>24}: {item.Delegates}\n'
            output+=f'{"Individual Contributions":>24}: {item.Contributions}\n'
            output+=f'{"Weekly News Coverage":>24}: {item.Coverage}\n\n'            
        print(output)


def gather_data():
    rcp_file = File("realclearpolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    nyt_file = File("nytimes.html")
    nyt_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    )
    nyt_web = Web(nyt_url, nyt_file)
    nyt = NYTimes(nyt_web)
    nyt.stats()


if __name__ == "__main__":
    gather_data()
    """url = "https://bites-data.s3.us-east-2.amazonaws.com/pycon2019.html"
    test_file = 'test_file.html'
    test_web = Web(url, File(test_file))
    print(test_web.url)
    print(test_web.file.name)
    print(test_web.file.path)
    print(test_web.file.data)
    print(test_web.data)
    print(test_web.soup)
    """
    
    
"""
assert "National Polling Average: 29%" in output
assert "       Pledged Delegates: 610" in output
assert "Individual Contributions: $11.1m" in output
assert "    Weekly News Coverage: 3" in output
"""    