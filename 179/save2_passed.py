SINGLE_LINE = '#'
INLINE = '  # '
MULTI_LINE = '"""'

def strip_comments(code):
    # see Bite description
    result=[]
    inside_multiline=False
    for line in code.splitlines():
        if inside_multiline:
            if MULTI_LINE in line:
                inside_multiline= False
            continue
        if line.lstrip().startswith(SINGLE_LINE):
            continue
        if INLINE in line:
            result.append(line[:line.find(INLINE)])
            continue
        if line.lstrip().startswith(MULTI_LINE):
            if MULTI_LINE in line.lstrip()[3:]:
                continue
            inside_multiline=True
            continue
       
        result.append(line)
    return "\n".join(result)


code = '''"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''   
    
    
print(strip_comments(code))