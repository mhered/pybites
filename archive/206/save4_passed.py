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
    
    
    ctx = decimal.getcontext()
    ctx.rounding = decimal.ROUND_HALF_EVEN
    
    
    item_total = decimal.Decimal(item_total.lstrip('$'))
    tax = item_total * decimal.Decimal(tax_rate.rstrip('%'))/decimal.Decimal('100')
    tax = tax.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_EVEN)
    print(tax)
    after_tax= item_total + tax 
    tip = after_tax * decimal.Decimal(tip.rstrip('%'))/decimal.Decimal('100')
    tip = tip.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_EVEN)
    print(tip)
    grand_total= after_tax + tip
    grand_total = grand_total.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_EVEN)
    per_person= grand_total / people
    per_person = per_person.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_EVEN)
    split=[per_person for _ in range(people)]
    split[0]+=grand_total-sum(split)
    grand_total=f'${grand_total}'
    
    return (grand_total, split)
    
    
print(check_split('$9.99', '3.25%', '10%', 2))  # ('$9.99', '3.25%', '10%', 2), expected = '$11.34' vs '$11.35'
print(check_split('$186.70', '6.75%', '18%', 6))  # ('$186.70', '6.75%', '18%', 6), expected = '$235.17' vs '$235.18'
print(check_split('$141.86', '2%', '18%', 9))  # ('$141.86', '2%', '18%', 9), expected = '$170.75' vs '$170.74'


