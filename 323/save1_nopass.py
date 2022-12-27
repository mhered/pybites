import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    sets=[set(arg) for arg in args if arg]
    result=sets[0]
    if len(sets)>1:
        for set_i in sets[1:]:
            result = result.intersection(set_i)
    return result

print(intersection({1,2,3}, {2,3,4}, {3,4}))
print(intersection([1,2,3,"1"], {1,-1}, {}))
print(intersection(None, "this is a string"))
