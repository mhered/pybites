import os
import urllib.request
import json
import ast
from pprint import pprint 

# this needed to do my testing with print, I am such a loser
# download file
tmp = os.getenv("TMP", "/tmp")
omdb_json = os.path.join(tmp, 'omdb')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/omdb_data',
    omdb_json)

# load file in list of dicts
with open(omdb_json,) as f:
    list_dicts = [ast.literal_eval(line) for line in f.readlines()]

# create JSON files from list of dicts
list_of_files=[]
for i, movie_dict in enumerate(list_dicts):
    filename = f"{tmp}/file_{i}.json" 
    with open(filename, "w") as outfile:
        json.dump(movie_dict, outfile)
    list_of_files.append(filename)

# print(list_of_files)


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    lst=[]
    for file in files:
        with open(file) as f:
            lst.append(json.load(f)) 
    return lst
    

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def _parse_num_nominations(string):
    return int(string.strip().split('&')[1].split()[0])
    
    
def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    
    nominations=dict((movie['Title'], _parse_num_nominations(movie['Awards']) ) for movie in movies)
    # print(runtimes)
    return max(nominations, key=nominations.get)

def _parse_runtime(string):
    return int(string.split()[0].strip())


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtimes=dict((movie['Title'], _parse_runtime(movie['Runtime']) ) for movie in movies)
    # print(runtimes)
    return max(runtimes, key=runtimes.get)

if __name__ == "__main__":

    lst=get_movie_data(list_of_files)
    print(lst)
    print(get_single_comedy(lst))
    print(get_movie_most_nominations(lst))
    print(get_movie_longest_runtime(lst))