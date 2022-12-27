from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        # do stuff before the original function gets called
        user=args[0]
        if user not in known_users:
            return 'please create an account'
        elif user not in loggedin_users:
            return 'please login'
        else:
            # call function
            return func(*args, **kwargs)
        # do stuff after function call 
    # return wrapper as a decorated function
    return wrapped


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
    
if __name__ == "__main__":
    print(welcome('anonimous'))