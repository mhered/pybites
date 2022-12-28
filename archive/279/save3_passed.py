def is_armstrong(n: int) -> bool:
    n_as_lst= [int(i) for i in str(n)]
    # print(n_as_lst)
    tmp = [i**len(n_as_lst) for i in n_as_lst]
    # print(tmp)
    return sum(tmp) == n

    

print(is_armstrong(8))