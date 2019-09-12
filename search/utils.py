def check_key(func):
    def wrapper(*args, **kwargs):
        if args[1] is None:
            raise ValueError('The key cannot be None.')
        return func(*args, **kwargs)
    return wrapper


def compare(a, b):
    return ((a > b) - (a < b)) 
