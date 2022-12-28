from collections import Counter 

def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    return _letters(word1) == _letters(word2) 
        
def _letters(word):
    return Counter([letter.lower() for letter in word if letter.isalpha() ])

"""
tests=[
    ("rail safety", "fairy tales"),
    ("roast beef", "eat for BSE"),
    ("restful", "fluster"),
    ("funeral", "real fun"),
    ("adultery", "true lady"),
    ("customers", "store scum"),
    ("forty five", "over fifty"),
    ("William Shakespeare", "I am a weakish speller"),
    ("Madam Curie", "Radium came"),
    ]
    
for word1, word2 in tests:
    print(is_anagram(word1, word2))
    
"""