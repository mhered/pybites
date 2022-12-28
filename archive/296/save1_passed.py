from typing import List
from itertools import zip_longest

def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    zipped = zip_longest(*lst_of_lst, fillvalue = fillvalue)
    return [list(item) for item in zip(*zipped)]

print(jagged_list([[1, 1, 1, 1], [0, 0, 0, 0], [1]], fillvalue=1))