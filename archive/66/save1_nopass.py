from itertools import accumulate
import operator

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums= accumulate(sequence, operator.add)
    avgs= (sum/(i+1) for i,sum in enumerate(sums))
    return avgs

# print(list(running_mean([1,2,3,4,5,6,7,8,9])))