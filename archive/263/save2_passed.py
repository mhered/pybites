from pprint import pprint

VERBOSE = False

def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    
    islands = 0         # var. for the counts
    nrows = len(grid)
    ncols = len(grid[0])
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                islands += 1
                if VERBOSE:
                    print(f"Found island number {islands}")
                mark_islands(i, j, grid)
    print (f"{islands} islands")
    return islands


def _print_grid(grid):
    nrows = len(grid)
    print("Exploring island:")
    for i in range(nrows):
        print(" ".join([str(el) for el in grid[i]]))
    print("\n")
    
    
def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    nrows = len(grid)
    ncols = len(grid[0])
    grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    if VERBOSE:
        _print_grid(grid)
    if i>0: 
        if grid[i-1][j] == 1:
            mark_islands(i-1, j, grid)
    if i<nrows-1:
        if grid[i+1][j] == 1:
            mark_islands(i+1, j, grid)
    if j>0:
        if grid[i][j-1] == 1:
            mark_islands(i, j-1, grid)
    if j<ncols-1:
        if grid[i][j+1] == 1:
            mark_islands(i, j+1, grid)

if __name__ == "__main__":
    
    test_grid = [[1, 0, 0, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 0, 0, 1]]
    
    count_islands(test_grid)
        