def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    
    r_rot = l_rot = 0
    
    if n<0:
        l_rot = -n
    else:
        r_rot = n
            
    return (string * 3)[len(string) + r_rot - l_rot : 2 * len(string) + r_rot - l_rot]
                    
print("5: ",rotate("thisisatest",5)) 
print("-2: ",rotate("thisisatest",-2)) 