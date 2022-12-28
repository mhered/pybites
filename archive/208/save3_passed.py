def find_number_pairs(numbers, N=10):

    return [(n1,n2) for i,n1 in enumerate(numbers) for n2 in numbers[i+1:] if n1+n2 == N]

    """ this works 
    lst = []
    for i,n1 in enumerate(numbers):
        for n2 in numbers[i+1:]:
            # print(f"{n1},{n2}")
            if n1+n2 == N:
                lst.append((n1,n2))
                
    return lst
    """
    
test2 = [0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31, 0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95]
print(find_number_pairs(test2, N=1))


