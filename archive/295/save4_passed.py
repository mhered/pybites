from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst)==0:
        return None
    joint_lst = [lst + [sep] for lst in lst_of_lst]
    return [item for sublist in joint_lst for item in sublist][:-1]

print(join_lists([ ['a']], '&'))
print(join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+'))