from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable

ALLOWED_OPERATORS = "+-*"
ALLOWED_NUMBERS = [1,2,3,4,5,6,7,8,9]

def _eval(operator_path, numbers):
    _operator_path = operator_path[:]
    _numbers = numbers[:]
    # print(f'{_operator_path=} {_numbers=}')

    while '*' in _operator_path:
        i = _operator_path.index('*')
        op = _operator_path.pop(i)
        # print(f'{op=} {i=}')
        _numbers[i]*=_numbers.pop(i+1)
        # print(f'{_operator_path=} {_numbers=}')
        
    while len(_operator_path)>0:
        op = _operator_path.pop(0)
        # print(f'{op=} {i=}')
        if op=='+':
            _numbers[0]+=_numbers.pop(1)
        if op=='-':
            _numbers[0]-=_numbers.pop(1)
        # print(f'{operator_path=} {numbers=}')
    return _numbers[0]


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # TODO: blank canvas to fill
    
    if not isinstance(expected_result, int):
        raise ValueError("Result must be of type int")
        
    if not all(op in ALLOWED_OPERATORS for op in operator_path):
        raise ValueError("Result must be of type int")
        
    num_ops=len(operator_path) + 1
    all_permutations = permutations(ALLOWED_NUMBERS, num_ops)
    
    return [list(perm) for perm in all_permutations if _eval(operator_path, list(perm)) == expected_result]
    
print(find_all_solutions(['+'],6))


# print(_eval(['*'],[3,2]))