from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    # you code ...
    cnt=Counter(numbers).most_common()
    major = cnt[0][0]
    minor = cnt[-1][0]
    
    return major, minor
    
    
print(major_n_minor([5,3,2,3,3,2,2,3,4,4]))
    
    