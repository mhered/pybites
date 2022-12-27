from typing import Generator

import json
import decimal

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    
    ctx = decimal.getcontext()
    ctx.rounding = decimal.ROUND_HALF_UP

    values = json.loads(values)
    values = [decimal.Decimal(str(value)) for value in values]
    for a,b in zip(values, values[1:]):
        c = a + b
        print(f"The sum of {a} and {b}, rounded to two decimal places, is {c:.2f}.")
        

calc_sums()