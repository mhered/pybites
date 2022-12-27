import math

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    func=math.ceil if up else math.floor
    return list(func(item) for item in transactions)
    

# t1 = [2.05, 3.55, 4.50, 10.76, 100.25]
# print(round_up_or_down(t1, False))