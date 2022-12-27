from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst)>1:
        joint_lst = [lst + [sep] for lst in lst_of_lst]
        print(joint_lst)
        flat_list = [item for sublist in joint_lst for item in sublist][:-1]
        print(flat_list)
    else:
        joint_lst = lst_of_lst 
    return joint_lst

print(join_lists([ ['a', 'b'], ['c'] ], '&'))
print(join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+'))