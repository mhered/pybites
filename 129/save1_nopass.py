import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0.0
    num=float(cap[1:-1])
    if cap[-1].lower() == 'b':
        num*=1000
    return num


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    return sum(_cap_str_to_mln_float(item['cap']) for item in data if item['industry'] == industry)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    symbol_and_cap_dict = dict((item['symbol'], _cap_str_to_mln_float(item['cap'])) for item in data )
    # print(symbol_and_cap_dict)
    return max(symbol_and_cap_dict, key=symbol_and_cap_dict.get)


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors_sorted_per_size = Counter(item['sector'] for item in data if item['sector'] != "n/a").most_common()
    return sectors_sorted_per_size[0][0], sectors_sorted_per_size[-1][0]

test = ['$1M', '$1B', 'n/a']
for item in test: 
    print(_cap_str_to_mln_float(item))
    
print(get_industry_cap("Medical/Dental Instruments"))
print(get_stock_symbol_with_highest_cap())
print(get_sectors_with_max_and_min_stocks())