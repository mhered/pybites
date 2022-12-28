import itertools
import os
import urllib.request

import functools
import operator
from pprint import pprint

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])
# pprint(list(word for word in dictionary if len(word)==2))

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
       
    return [word for word in _get_permutations_draw(draw) if word.lower() in dictionary]

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = list(map(lambda x: x.lower(), draw))
    nested_lst= [itertools.permutations(draw,r=l) for l in range(2,len(draw)+1)]
    lst_of_tups = functools.reduce(operator.iconcat, nested_lst, [])
    return ["".join(elem) for elem in lst_of_tups]
    

"""
draw= ['G', 'A', 'R', 'Y', 'T', 'E', 'V' ]
print(_get_permutations_draw(draw))
print(get_possible_dict_words(draw))
"""