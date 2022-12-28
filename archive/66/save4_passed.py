from itertools import accumulate
import operator

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return (round(part_sum/(i+1),2) for i, part_sum in enumerate(accumulate(sequence, operator.add)))

# print(list(running_mean([1,2,4,9,11,26])))