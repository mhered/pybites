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
                result.setdefault(director,[]).append(Movie(title=title, year=year, score=score))
    return result
        

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    tmp = [movie.score for movie in movies]
    return round(sum(tmp)/len(tmp),1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    return [(director, calc_mean_score(movie_list)) for director, movie_list in directors.items() if len(movie_list) > MIN_MOVIES]

if __name__ == "__main__":
    
    a= get_movies_by_director()
    
    pprint(a['George Lucas'])
    print(calc_mean_score(a['George Lucas']))
    
    pprint(get_average_scores(a))