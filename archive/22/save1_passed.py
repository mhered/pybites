from functools import wraps


def make_html(element):
    
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return f"<{element}>" + fn(*args, **kwargs) + f"</{element}>"
        return wrapper
    return decorate


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
    
print(get_text("a test"))