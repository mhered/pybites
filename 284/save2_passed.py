from typing import List
from math import factorial, ceil

def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    # return row
    
    row = N-1
    result=[0 for _ in range(N)]

    for col in range(ceil(N/2)):
        result[col]=int(factorial(row)/(factorial(row-col)*factorial(col)))
        result[-col-1]=result[col]
    return result
        
print(pascal(5))