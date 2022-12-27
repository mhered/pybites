import string
import unicodedata

def _non_ascii_char(c):
    # non-ascii number 
    if unicodedata.category(c) in ['Nd']:
        if c not in string.digits:
            return True
    # non-ascii letter
    if unicodedata.category(c) not in ['Po', 'Pd']: 
        if c.lower() not in string.ascii_lowercase:
            return True
    return False
    
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    result=[]
    for word in text.split():
        print(word)
        for c in word.strip():

            if _non_ascii_char(c): 
                print(word)
                result.append(word)
                break
                
    return result
    
print(extract_non_ascii_words('He wonede at Ernleȝe at æðelen are chirechen'))

