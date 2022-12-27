import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    return pprint.pformat(obj, width=60, depth = 2, sort_dicts= True)
    
d={"Z": "Z"*40,
       "B": [1,[2,[3]]],
       "A": "A"*40}
print(d)
print(pretty_string(d))