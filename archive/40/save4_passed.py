import string 

def binary_search(sequence, target):
    start = 0
    end = len(sequence)
    while start<=end:
        midp=(end+start)//2

        if sequence[midp]==target: 
            return midp

        if sequence[midp]<target: 
            start = midp+1
            continue

        if sequence[midp]>target: 
            end = midp-1
            continue
    return None
