def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """

    # TODO: Your code
    lst = [number for number, frequency in sorted(d.items()) for _ in range(frequency) ]
    mid_pt= len(lst)//2
    if len(lst)%2!=0:
        return lst[mid_pt]
    else:
        return (lst[mid_pt-1] + lst[mid_pt])/2
        
print(calc_median_from_dict({1: 2, 3: 1, 4: 2}))