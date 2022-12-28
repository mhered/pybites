from typing import Generator

import json
from decimal import Decimal

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values = json.loads(values)
    values = [Decimal(str(value)) for value in values]
    for a,b in zip(values, values[1:]):
        c = round(a + b,2)
        yield f"The sum of {a} and {b}, rounded to two decimal places, is {c}."
        
# calc_sums()