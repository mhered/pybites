import textwrap
import itertools 
from pprint import pprint 

COL_WIDTH = 20
COL_MARGIN = 4


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""

    paragraphs = text.split('\n\n')
    
    paragraphs_wrapped = [textwrap.wrap(par.strip(), width=COL_WIDTH) for par in paragraphs]

    lines_zipped_by_column= list(itertools.zip_longest(*paragraphs_wrapped, fillvalue=""))

    result = []
    for line in lines_zipped_by_column:
        result.append("".join(col.ljust(COL_WIDTH+COL_MARGIN) for col in line))
    return "\n".join(result)
    
    
text = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""
    
pprint(text_to_columns(text))