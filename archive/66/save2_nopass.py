from itertools import accumulate
import operator

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return (sum/(i+1) for i,sum in enumerate(accumulate(sequence, operator.add)))

# print(list(running_mean([1,2,3,4,5,6,7,8,9])))