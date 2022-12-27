from typing import List

EAST = "E"
WEST = "W"


def _has_a_view(i, buildings, direction):
    if direction.upper() == 'W':
        if i == 0:
            return True
        subset = buildings[:i]
    elif direction.upper() == 'E':
        if i == len(buildings):
            return True
        subset = buildings[i+1:]
    else:
        raise ValueError("Direction should be 'W' or 'E'")
        
    return all(b<buildings[i] for b in subset)

def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    return [i for i in range(len(buildings)) if _has_a_view(i, buildings, direction)]


if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
    
    

        
