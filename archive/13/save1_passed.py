from collections import namedtuple
from datetime import datetime
import json
from pprint import pprint


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    Blog = namedtuple('Blog', dict_.keys())
    return Blog(**dict_)


def nt2json(nt):
    return json.dumps(nt._asdict(), indent = 4, default=str) 


nt=dict2nt(blog)
pprint(nt2json(nt))

