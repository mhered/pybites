CM_PER_INCH=2.54
def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) not in [int, float]:
        raise TypeError
    if not isinstance(fmt,str) or fmt.lower() not in ["cm", "in"]:
        raise ValueError
    if fmt.lower() == "cm":
        result = value * CM_PER_INCH
    if fmt-lower() == "in":
        result = value / CM_PER_INCH
    
    return round(result,4)