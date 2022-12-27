import string
import unicodedata

def _non_ascii_char(c):
    # non-ascii number: it is a number but not an ascii number 
    if unicodedata.category(c) in ['Nd'] and c not in string.digits:
            return True
    # non-ascii letter: it is not punctuation or number (i.e. it is a letter) but not an ascii letter
    if unicodedata.category(c) not in ['Po', 'Pd', 'Nd'] and c.lower() not in string.ascii_lowercase:
            return True
    return False
    
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if any(_non_ascii_char(c) for c in word.strip())]

