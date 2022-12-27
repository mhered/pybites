import string
IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    lst=[] 
    for name in names:
        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        if name.startswith(QUIT_CHAR):
            break
        lst.append(name)
        if len(lst) >= MAX_NAMES:
            break
    return lst

lst=['pet1e', 'milly', 'quit', 'me', 'you' ]
print(filter_names(lst))