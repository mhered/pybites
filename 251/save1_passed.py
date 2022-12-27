import string

import pandas as pd


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    return pd.Series([1, 2, 3, 4, 5], name="Fred", dtype='int64')


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    PRECISION = 1000
    lst=[i/PRECISION for i in range(PRECISION+1)]
    return pd.Series(lst, dtype='float64')


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    gen=((label,value) for value, label in enumerate(string.ascii_lowercase, start=1))
    return pd.Series(dict(gen), dtype='int64')

def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    gen=((label,value) for label,value in enumerate(string.ascii_uppercase, start=101))
    return pd.Series(dict(gen), dtype='object')


print(float_series())
print(alpha_index_series())
print(object_values_series())