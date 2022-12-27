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
    word=re.sub('(?<=[a-z])(?=[0-9])|(?<=[0-9])(?=[a-z])', '_', word)
    return word

def snake_case_keys(data):

    if isinstance(data, dict):
        data_list = [data]
    elif isinstance(data,list):
        data_list = data

    for i,data in enumerate(data_list):
        if isinstance(data,dict):
            data = {_make_snake(key): value for key,value in data.items()}
            for key, value in data.items():
                if isinstance(value, dict) or isinstance(value, list):
                    data[key]= snake_case_keys(value)
    
            data_list[i] = data
        
    return data_list if len(data_list)>1 else data_list[0]
        

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
    "random": [
                "Luke",
                [
                    "blowing up the death star",
                    {"skillName": "bulls-eye womprats",
                     "skillParameters": "with my T47"},
                ],
            ]
}

pprint(snake_case_keys(data))