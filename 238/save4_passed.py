from fibonacci import fib

import pytest

# write one or more pytest functions below, they need to start with test_
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


def test_n_negative():
    # fib(-1) ValueError
    with pytest.raises(ValueError):
        fib(-1)


def test_n_0():
    fib_lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for (i, expected) in enumerate(fib_lst):
        assert fib(i) == expected



