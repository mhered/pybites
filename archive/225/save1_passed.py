PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    result=[]
    for letter in text:
        if letter in PYBITES:
            letter = letter.upper()
        elif letter in PYBITES.upper():
            letter = letter.lower()
        result.append(letter)
    return "".join(result)
    
text = "Today we added TWO NEW Bites to our Platform, exciting!"
print(convert_pybites_chars(text))