#!/usr/bin/env python

import os
import urllib.request
from operator import itemgetter

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding


def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    lst = []
    with open(DICTIONARY) as dict:
        for word in dict:
            lst.append(word.strip())
    return lst


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for letter in word.strip().upper():
        for group in scrabble_scores:
            if letter in group[1]:
                score += group[0]
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    lst = [(word, calc_word_value(word)) for word in words]
    return max(lst, key=itemgetter(1))[0]


print(list(load_words()))

print(f"{calc_word_value('bob')} should be == 7")
print(f"{calc_word_value('JuliaN')} should be == 13")
print(f"{calc_word_value('PyBites')} should be == 14")
print(f"{calc_word_value('benzalphenylhydrazone')} should be == 56")

print(max_word_value(['bob', 'benzalphenylhydrazone', 'julian', 'pybites']))
