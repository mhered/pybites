num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    result = sum(numbers)
    num_hundreds+= result//100
    return result


"""
for i in range(5):
    print(sum_numbers([10, 50, 90]))
    print(f"{num_hundreds=}")
"""