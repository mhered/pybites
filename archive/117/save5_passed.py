def round_even(number):
    """Takes a number and returns it rounded even"""
    decimal_part = number % 1
    int_part = number - decimal_part
    if decimal_part < 0.5:
        return int_part
    if decimal_part > 0.5:
        return int_part + 1
    if decimal_part == 0.5:
        if int_part%2 == 0:
            return int_part
        return int_part + 1

    
    
