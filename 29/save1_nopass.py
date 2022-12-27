from collections import Counter

alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

test1= ['A', 'f', '.', 'Q', 2] 
test2= ['.', '{', ' ^', '%', 'a'] 

def get_index_different_char(chars):
    is_alphanumeric = [(i, str(char) in alphanumeric) for i, char in enumerate(chars)]

    if Counter([item[1] for item in is_alphanumeric])[True] == 1:
        # alphanumeric is the different one
        index = [item[0] for item in is_alphanumeric if item[1]==True]
    else:
        # non-alphanumeric is the different one
        index = [item[0] for item in is_alphanumeric if item[1]==False]
    return is_alphanumeric[index[0]][0]


print(get_index_different_char(test1))
print(get_index_different_char(test2))