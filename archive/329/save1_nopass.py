from pprint import pprint
import string
import re
    
def _make_snake(word):
    # replace - with _
    # make [0] lower
    # replace upper with _lower
    if len(word)<2:
        return word.lower()
    result = [word[0].lower()]
    for letter in word[1:]:
        if  letter =='-':
            result.append('_')
        elif letter in string.ascii_uppercase:
            result.append('_'+letter.lower())
        else:
            result.append(letter)
    word="".join(result)
    word=re.sub('(?<=[a-z])(?=\d)|(?<=\d)(?=[a-z])', '_', word)
    return word

def snake_case_keys(data):
    return {_make_snake(key): value for key,value in data.items()}
        

data={
    "camelCase": "Value1",
    "camelcase": "Value1",
    "PascalCase": "Value2",
    "kebab-case": "Value3",
    "ACRONYM": "Value4",
    "number22": "Value5"
}

pprint(snake_case_keys(data))