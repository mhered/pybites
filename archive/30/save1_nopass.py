import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from pprint import pprint

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)



MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    
    FIELDS = {'director_name', 'movie_title', 'title_year', 'imdb_score'}
    with open(local, newline='') as f:
        data = csv.DictReader(f)
        result = {}
        for row in data:
            year = row.get('title_year', None)
            if year and int(year) >= MIN_YEAR:
                director = row['director_name']
                title = row['movie_title'].strip()
                score = float(row['imdb_score'])
                year = int(year)
                if director in result.keys():
                    result[director].append(Movie(title=title, year=year, score=score))
                else:
                    result[director]= [Movie(title=title, year=year, score=score)]
    return result
        


"""
extract director_name, movie_title, title_year, imdb_score
ignore movies without all of these fields.
Type conversions: title_year -> int / imdb_score -> float
Discard any movies older than 1960.
"""


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    pass


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    pass


# pprint(get_movies_by_director())
