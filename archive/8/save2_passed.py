def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    l=len(string)
    n = n % l
    return (string * 3)[l + n : 2 * l + n]
                    
print("5: ",rotate("0123456789",5)) 
print("-2: ",rotate("0123456789",-2)) 
print("-12: ",rotate("0123456789",-12)) 
print("10: ",rotate("0123456789",10)) 