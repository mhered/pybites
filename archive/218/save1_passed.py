from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        # do stuff before the original function gets called
        print(UPPER_SLICE)
        # call function
        result = func(*args, **kwargs)
        # do stuff after function call 
        print(LOWER_SLICE)
        # return the result
        # return result
    # return wrapper as a decorated function
    return wrapped
    
    
if __name__ == "__main__":
    
    @sandwich
    def add_ingredients(ingredients):
        print(' / '.join(ingredients))

    ingredients = ['bacon', 'lettuce', 'tomato']
    add_ingredients(ingredients)