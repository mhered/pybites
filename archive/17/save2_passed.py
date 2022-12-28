from itertools import permutations, combinations

def friends_teams(friends_list, team_size:int = 2, order_does_matter:bool = False):
    if order_does_matter:
        return permutations(friends_list,team_size)
    else:
        return combinations(friends_list,team_size)
        
        
friends = 'Bob Dante Julian Martin'.split()

print(list(friends_teams(friends, team_size = 3, order_does_matter = False)))