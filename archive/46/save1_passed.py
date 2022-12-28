from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num%5 == 0 and num%3 == 0:
        result = "Fizz Buzz"
    elif num%3 == 0:
        result = "Fizz"
    elif num%5 == 0:
        result = "Buzz"
    else: 
        result = num
    return result

print(", ".join(str(fizzbuzz(i)) for i in range(1,30)))

# print([fizzbuzz(i) for i in range(1,30)])
