from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        # do stuff before the original function gets called

        for arg in args:
            if not isinstance(arg,int):
                raise TypeError
            if arg < 0:
                raise ValueError
        return func(*args)

    # return wrapper as a decorated function
    return wrapped

@int_args
def test_int(*args):
    for arg in args: 
        print(arg)

if __name__ == "__main__":
    test_int(1,2,3,4,-5)