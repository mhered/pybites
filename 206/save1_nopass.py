import decimal

def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    """
    ctx = decimal.getcontext()
    ctx.rounding = decimal.ROUND_HALF_EVEN
    """
    
    item_total = decimal.Decimal(item_total.lstrip('$'))
    tax = item_total * decimal.Decimal(tax_rate.rstrip('%'))/100
    after_tax= item_total + tax 
    tip = after_tax * decimal.Decimal(tip.rstrip('%'))/100
    grand_total= round(after_tax + tip,2)
    
    per_person= round(grand_total / people,2)
    split=[per_person for _ in range(people)]
    split[0]+=grand_total-sum(split)
    grand_total=f'${grand_total}'
    
    return (grand_total, split)
    
    
print(check_split('$9.99', '3.25%', '10%', 2))  # ('$9.99', '3.25%', '10%', 2), expected = '$11.34'
print(check_split('$186.70', '6.75%', '18%', 6))  # ('$186.70', '6.75%', '18%', 6), expected = '$235.17'
print(check_split('$141.86', '2%', '18%', 9))  # ('$141.86', '2%', '18%', 9), expected = '$170.75'


