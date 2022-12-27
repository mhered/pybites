from itertools import permutations, combinations

def friends_teams(friends_list, team_size:int = 2, order_does_matter:bool = False):
    return permutations(friends_list,team_size) \
        if order_does_matter else \
        combinations(friends_list,team_size)
        
        
friends = 'Bob Dante Julian Martin'.split()

print(list(friends_teams(friends,order_does_matter = True)))