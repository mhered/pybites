from collections import Counter

alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

test1= ['A', 'f', '.', 'Q', 2] 
test2= ['.', '{', ' ^', '%', 'a'] 
test3 = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']

def get_index_different_char(chars):
    is_alphanumeric = [str(char) in alphanumeric and len(str(char))>0 for char in chars]
    # print("is_alphanumeric=",is_alphanumeric)
    counter = Counter(is_alphanumeric).most_common(1)
    # print("counter=",counter)
    least_common = not counter[0][0]
    # print("least_common=",least_common)
    return [i for i,item in enumerate(is_alphanumeric) if item==least_common][0]

    
    """ alternative that also works
    is_alphanumeric = [(i, str(char) in alphanumeric and len(str(char))>0) for i, char in enumerate(chars)]

    if Counter([item[1] for item in is_alphanumeric])[True] == 1:
        # alphanumeric is the different one
        index = [item[0] for item in is_alphanumeric if item[1]==True]
    else:
        # non-alphanumeric is the different one
        index = [item[0] for item in is_alphanumeric if item[1]==False]
    return is_alphanumeric[index[0]][0]
    """



print(get_index_different_char(test1))
print(get_index_different_char(test2))
print(get_index_different_char(test3))