def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    if number <= base:
        return int(str(number//base) +str(number%base))
    else:
        return int(dec_to_base(number//base, base) +str(number%base))

print(dec_to_base(256,8))