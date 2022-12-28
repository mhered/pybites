import string

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    numbers=sorted([word for word in words if word[0] in string.digits], key=str.casefold)
    return sorted([word for word in words if word not in numbers], key=str.casefold)+numbers
    
words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()

print(sort_words_case_insensitively(words))