# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_shores(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    nums = 0
    rows= len(map_)
    cols= (len(map_[0]))
    # your code here
    # print(f"{r=},{c=}")
    #check N
    if r==0:
        nums+=1
    else:
        nums+=map_[r-1][c]==0
    
    #check S
    if r==rows-1:
        nums+=1
    else:
        nums+=map_[r+1][c]==0

    #check E
    if c==0:
        nums+=1
    else:
        nums+=map_[r][c-1]==0

    #check W
    if c==cols-1:
        nums+=1
    else:
        nums+=map_[r][c+1]==0
    
    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    rows= len(map_)
    cols= (len(map_[0]))
    # your code here
    for i in range(rows):
        for j in range(cols):
            if map_[i][j] == 1:
                perimeter +=get_shores(map_, i, j) 
    return perimeter
    
    
