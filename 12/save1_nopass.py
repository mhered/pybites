from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    """Raised when the user does not exist"""
    pass

class UserAccessExpired(Exception):
    """Raised when user access is expired"""
    pass

class UserNoPermission(Exception):
    """Raised when the user is not Admin"""
    pass

def get_secret_token(username):
    if username not in USERS:
        raise UserDoesNotExist
    if username.expired:
        raise AccessExpired
    if not username.role == ADMIN:
        raise UserNoPermission
    return SECRET
    

# get_secret_token('Tim')
# get_secret_token('Bob')
# get_secret_token('Julian')
# print(get_secret_token('PyBites'))