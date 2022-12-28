import re
from pprint import pprint

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

def _find_value(value, matrix_2d):
    nrows = len(matrix_2d)
    ncols = len(matrix_2d[0])
    for i in range(nrows):
        for j in range(ncols):
            if matrix_2d[i][j] == value:
                return [i, j]

def _search(value, i,j, matrix_2d):
    nrows = len(matrix_2d)
    ncols = len(matrix_2d[0])
    if i>0:
        if matrix_2d[i-1][j] == value:
            return UP, i-1, j
    if i<nrows-1:
        if matrix_2d[i+1][j] == value:
            return DOWN, i+1, j
    if j>0:
        if matrix_2d[i][j-1] == value:
            return LEFT, i, j-1
    if j<ncols-1:
        if matrix_2d[i][j+1] == value:
            return RIGHT, i, j+1
    return None, i, j




def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    data=[]
    for line in grid.splitlines():
        row= re.findall('[0-9]+',line)
        if row:
            data.append([int(n) for n in row])
    # pprint(data)
    
    nrows, ncols = len(data), len(row)
    
    if not start_coordinates:
        start_coordinates = _find_value(START_VALUE, data)
    i,j= tuple(start_coordinates)
    # print(f"Starting at {i} {j}")

    value = data[i][j]
    direction = new_direction = RIGHT
    
    print(f"{value}",end=" ")
    
    while True:
# look up for N+1
        value+=1
        new_direction, i,j = _search(value, i,j, data)
        if not new_direction:
            break
        # update direction and print
        if new_direction != direction:
            direction = new_direction
            print(new_direction)         
        # print value
        print(f"{value}",end=" ")
    
test ="""
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

print_sequence_route(test)


"""
1 2 ⇓
3 ⇐
4 5 ⇑
6 7 ⇒
8 9 10 ⇓
11 12 13 ⇐
14 15 16 17 ⇑
18 19 20 21 ⇒
22 23 24 25
"""