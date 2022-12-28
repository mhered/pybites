from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    result=[]
    for num in numbers:
        num_n_digit=int(re.sub('.-','',str(num)).ljust(n,'0'))
        if num<0:
            num_n_digit*=-1
        result.append(num_n_digit)
    return result
    
