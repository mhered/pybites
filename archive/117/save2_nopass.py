def round_even(number):
    """Takes a number and returns it rounded even"""
    int_part = floor(number)
    decimal_part = number - int_part
    if decimal_part == 0.5:
        if floor(number)%2 == 0:
            return int_part
        return int_part + 1
    return round(number)
    
    
