from math import ceil

def round_to_next(number: int, multiple: int):
    return ceil(number/multiple)*multiple
    

nums = [0,2,5,42,-6,-6]
mults = [5,5,5,5,-10,-10]

for num,mult in zip(nums,mults):
    print(f'{num=} -> {mult=} = {round_to_next(num,mult)}')