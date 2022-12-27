def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    for i,letter in enumerate(text):
        if letter !=" ":
            return i
    # only spaces found
    return len(text)
    
print(count_indents("   n"))