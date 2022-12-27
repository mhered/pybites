def find_number_pairs(numbers, N=10):
    lst = []
    for i in numbers:
        for j in numbers[(i+1):]:
            if i+j == N:
                lst.append((i,j))
                
    return lst