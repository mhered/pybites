def strip_comments(code):
    # see Bite description
    pass


code = """this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
    
    
    
print(strip_comments(code))