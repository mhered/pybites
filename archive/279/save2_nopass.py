def is_armstrong(n: int) -> bool:
    n_as_lst= [int(i) for i in str(n)]
    if len(n_as_lst) == 1: 
        return True
    return  sum([i**3 for i in n_as_lst]) == n

    

# print(is_armstrong(9474))