"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import string

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def _as_stripped_list(word):
    return [letter for letter in word.lower() if letter in string.ascii_lowercase]

def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    stripped_lst = _as_stripped_list(word)
    return stripped_lst == list(reversed(stripped_lst))


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = load_dictionary()
    
    longest_palindrome ="" 
    length= 0
    for word in words:
        if is_palindrome(word):
            len_lst = len(_as_stripped_list(word))
            if len_lst > length:
                longest_palindrome = word
                length = len_lst
    return longest_palindrome

print(is_palindrome("No 'x' in 'Nixon'"))

word_list ="""
Aibohphobia
'Avid diva
Avid diva. 
A Toyota’s a Toyota.
A man, a plan, a canal: Panama
No 'x in 'Nixon'
malayalam
PyBites
toyota
palindrome
"""
print(get_longest_palindrome(word_list.splitlines()))
