PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return "".join([letter for letter in input_string if letter not in PUNCTUATION])

print(remove_punctuation("Some other (chars) |:-^, let's delete them"))