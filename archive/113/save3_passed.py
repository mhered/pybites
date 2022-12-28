import string
import unicodedata

def _non_ascii_char(c):
    # non-ascii number 
    if unicodedata.category(c) in ['Nd'] and c not in string.digits:
            # print("non-ascii number: ",c)
            return True
    # non-ascii letter
    if unicodedata.category(c) not in ['Po', 'Pd', 'Nd'] and c.lower() not in string.ascii_lowercase:
            # print("non-ascii letter: ",c)
            return True
    return False
    
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    result=[]
    for word in text.split():
        for c in word.strip():
            if _non_ascii_char(c):
                # print("...in: ",word)
                result.append(word)
                break
                
    return result
    
print(extract_non_ascii_words('He wonede at Ernleȝe at æðelen are chirechen'))
print(extract_non_ascii_words('Over \u0e55\u0e57 57 flavours'))
