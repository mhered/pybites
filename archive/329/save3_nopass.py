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
    data = {_make_snake(key): value for key,value in data.items()}
    
    for key, value in data.items():
        if isinstance(value, dict):
            data[key]= snake_case_keys(value)
        if isinstance(value, list):
            for i,item in enumerate(value):
                if isinstance(item,dict):
                    data[key][i]= snake_case_keys(item)
    return data
        

data={
    "camelCase": "Value1",
    "camelcase": "Value1",
    "PascalCase": "Value2",
    "kebab-case": "Value3",
    "ACRONYM": "Value4",
    "number22": {
                "helmetColor": "black",
                "armorColor": "black",
                "capeColor": "black",
            },
    "nested_list": [{"firstName": "Luke"},
                     {"firstName": "Leia"}],
}

pprint(snake_case_keys(data))