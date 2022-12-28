import string
from itertools import cycle

def sequence_generator():
    lst=zip(enumerate(string.ascii_uppercase,1))
    lst=list(sum(lst,())) # flatten tuples
    lst=list(sum(lst,())) # flatten tuples again
    
    for item in cycle(lst):
        yield item

a=sequence_generator()

for _ in range(60):
    print(next(a))
