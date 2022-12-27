from typing import List, TypeVar
T = TypeVar('T', int, float)
import re

def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    result=[]
    for num in numbers:
        num_n_digit=int(re.sub('\.|-','',str(num)).ljust(n,'0')[:n])
        if num<0:
            num_n_digit*=-1
        result.append(num_n_digit)
    return result
    
"""
[], 1, []
[1, 2, 3], 1, [1, 2, 3]
[1, 2, 3], 2, [10, 20, 30]
[0, 1, 2, 3], 2, [0, 10, 20, 30]
[8, 9, 10], 2, [80, 90, 10]
[5.2, 1600, 520, 3600, 13, 55, 4000], 2, [52, 16, 52, 36, 13, 55, 40]
[-1.1, 2.22, -3.333], 3, [-110, 222, -333]
"""

print(n_digit_numbers([-1.1, 2.22, -3.333], 3))