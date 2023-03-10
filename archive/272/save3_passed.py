from collections import Counter

from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    sentence2_lower = [word.lower() for word in sentence2]
    
    result = set(word.lower() for word in sentence1 if word.lower() in sentence2_lower)
    
    return sorted(result,key=len)
    

S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything', 'do']
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act', 'do']
print(common_words(S,T))