from typing import Sequence
from collections import Counter

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"

def _check_valid_input(citations):
    if citations is None:
        raise ValueError(VALUE_ERROR_MSG)
        
    if not isinstance(citations, (list, tuple)):
        raise TypeError(TYPE_ERROR_MSG)
    
    if not citaions or any(not isinstance(item, int) or item<0 for item in citations):
        raise ValueError(VALUE_ERROR_MSG)


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
    _check_valid_input(citations)
    
    count = Counter(citations)

    for i in range(len(citations),0,-1):
        if sum(n_papers for n_citations, n_papers in count.items() if n_citations >=i) >= i:
            return i


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""
    _check_valid_input(citations)

    count = Counter(citations)
    return sum(n_papers for n_citations, n_papers in count.items() if n_citations >=10)
    

print(h_index([0, 0, 11, 1, 10, 5, 10, 5]))

print(i10_index([0, 0, 11, 1, 10, 5, 10, 3]))