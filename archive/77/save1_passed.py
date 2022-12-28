def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities) ^ set(other_cities))


if __name__ == "__main__":
    a = ['1','2','3','4','5','6']
    b= ['3','4','5','6','7','8']
    
    print(uncommon_cities(a,b))