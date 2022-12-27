import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    is_valid = re.match('^PB(-([A-Z0-9]){8}){4}$',key.upper())
    return bool(is_valid)
    
print(validate_license('Pb-U82N45EH-PG65P 87-IXPWQG5T-898XSZI4'))