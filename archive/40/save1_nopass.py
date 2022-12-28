import string 

def binary_search(sequence, target):
    start = 0
    end = len(sequence)
    while start<end:
        midp=(end+start)//2

        if sequence[midp]==target: 
            return midp

        if sequence[midp]<target: 
            start = midp
            continue

        if sequence[midp]>target: 
            end = midp
            continue
    return None
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

print(binary_search(PRIMES, 59))