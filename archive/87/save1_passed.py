def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    UNITS = {0: '', 1:'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8:'VIII', 9:'IX' }
    TENS = {0: '', 1:'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8:'LXXX', 9:'XC' }
    HUNDREDS = {0: '', 1:'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8:'DCCC', 9:'CM' }
    
    if not isinstance(decimal_number,int) or not 0<=decimal_number<=4000:
        raise ValueError
    
    figures= [int(c) for c in str(decimal_number)[::-1]]
    
    result = ''
    result+='M'*figures[3] if len(figures)>3 else '' 
    result+=HUNDREDS[figures[2]] if len(figures)>2 else ''
    result+=TENS[figures[1]] if len(figures)>1 else ''
    result+=UNITS[figures[0]] if len(figures)>0 else ''  
    return result


    

print(romanize(1234))