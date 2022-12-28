from typing import Tuple
import string
from collections import Counter
NOT_LETTER = string.punctuation + string.digits
import unicodedata



def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if not isinstance(text, str):
        raise ValueError
        
    lst=[]
    for word in text.split():
        if word: 
            word_stripped_as_lst=[c for c in word.casefold() if unicodedata.category(c) not in ['Po', 'Pd', 'Nd']]
            if word_stripped_as_lst:
                top_letter, count = Counter(word_stripped_as_lst).most_common()[0]
                lst.append((word.strip(NOT_LETTER), top_letter, count))
    if lst:
        return max(lst,key= lambda x:x[2])
    else:
        return ('', '', 0)

if __name__== '__main__':
    
    test = ['emoji like 😃😃😃😃 are not letters',
    'Société Générale est une des principales banques françaises',
    'Short Plays By Lady Gregory The Knickerbocker Press 1916',
    'six-feet-two in height',
    'der Schloß is riesig',
    'the quick brown fox jumped over the lazy dog',
    '«¿Tiene sentido la TV pública?»',
    "but we've been there already!!!",
    '"____".isalpha() is True, thus this test text',
    '99abc99 __abc__ --abc-- digits _ and - are not letters',
    'test test test test test correct-answer.',
    'They shouted "Oh no she didn\'t"',
    "The brothers' feet were muddy.",
    '1, 2, 3',
    '',
    ]
    
    for item in test: 
        print(max_letter_word(item))