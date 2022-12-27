import string
import unicodedata

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    result=[]
    for word in text.split():
        print(word)
        for c in word.strip():
            # non-ascii number or non-ascii letter
            if (unicodedata.category(c) in ['Nd'] and c not in string.digits) or \
            (unicodedata.category(c) not in ['Po', 'Pd'] and c.lower() not in string.ascii_lowercase): 
                print(word)
                result.append(word)
                break
                
    return result
    
print(extract_non_ascii_words('He wonede at Ernleȝe at æðelen are chirechen'))

