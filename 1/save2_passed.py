def sum_numbers(numbers=None):
    if numbers is None:
        numbers = list(range(1,101))
    return sum(numbers)
    
lst= list(range(1,10))
print(lst)
print(sum_numbers(lst))
print(sum_numbers(None))
print(sum_numbers([]))
