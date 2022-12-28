from typing import List
from itertools import permutations

def _int_from_digits(digits:tuple):
    return int("".join(str(n) for n in digits))
    
    
def minimum_number(digits: List[int]) -> int:
    return min(_int_from_digits(item) for item in list(permutations(set(digits))))

test=[1,9,5,9,1]
print(minimum_number(test))