from dataclasses import dataclass

import dateutil


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
    actor_born=dateutil.parser.parse(actor.born, fuzzy=True)
    movie_released=dateutil.parser.parse(movie.release_date, fuzzy=True)
    age=dateutil.relativedelta.relativedelta(movie_released-actor_born).years
    return f"{actor.name} was {age} years old when {movie.title} came out."