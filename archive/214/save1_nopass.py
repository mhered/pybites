def countdown():
    """Write a generator that counts from 100 to 1"""
    COUNT = 100
    for i in range(COUNT):
        yield COUNT-i
    raise StopIteration
    
"""test for COUNT =5
cd = countdown()
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

next(cd)
"""