from operator import itemgetter

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    processed_names= []
    for name in names:
        name = name.title()
        if name not in processed_names:
            processed_names.append(name)
    return processed_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names_list= []
    for name in names:
        name=name.split()
        names_list.append([name[0],name[1]])
    names_list.sort(key=lambda x:x[1], reverse=True)
    processed_names=[]
    for name_surname in names_list:
        processed_names.append(" ".join(name_surname))
    return processed_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    clean_names = dedup_and_title_case_names(names)
    shortest_name= ""
    shortest_length=len(names)+1
    for name in clean_names:
        name=name.split()
        if len(name[0])<shortest_length:
            shortest_name= name[0]
            shortest_length= len(shortest_name) 
    return shortest_name

    
print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
