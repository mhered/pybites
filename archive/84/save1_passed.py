def flatten(list_of_lists):
    flat = []
    for item in list_of_lists:
        if isinstance(item, list) or isinstance(item,tuple):
            for subitem in flatten(item):
                flat.append(subitem) 
        else:
            flat.append(item)
    return flat

test =[1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]

print(flatten(test))