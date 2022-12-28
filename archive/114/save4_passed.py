import os
import sys
import urllib.request
import string

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    
    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)

    @staticmethod
    def hex2rgb(h):
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(h,str):
            raise ValueError("not a string")
        if not h[0]=="#":
            raise ValueError("missing #")
        if not len(h[1:])==6:
            raise ValueError("wrong length")
        if not all(c in string.hexdigits for c in h[1:]):
            raise ValueError("some characters are not hex")

        return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

    @staticmethod
    def rgb2hex(r):
        """Class method that converts an rgb value into a hex one"""
        if isinstance(r, tuple) and len(r) == 3 and all(isinstance(n,int) and 0<=n<=255 for n in r): 
            return '#%02x%02x%02x' % r
        else:
            raise ValueError
            

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"
        
print(COLOR_NAMES['white'.upper()])