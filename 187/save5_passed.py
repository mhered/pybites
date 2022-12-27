from dataclasses import dataclass

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    actor_born=parse(actor.born, fuzzy=True)
    movie_released=parse(movie.release_date, fuzzy=True)
    
    age=relativedelta(movie_released,actor_born).years
    return f"{actor.name} was {age} years old when {movie.title} came out."
    
    
"""
actor=Actor('Michelle Pfeiffer', 'April 29, 1958')
movie=Movie('New Jack City', 'January 17, 1991')
print(get_age(actor, movie) )
"""