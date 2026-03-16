import datetime
from functools import wraps

def validate_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        for argument in args:
            if not isinstance(argument, (int, float)):
                raise TypeError("Error, must be a number format.")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("Error, must be a number format.")

        results = func(*args, **kwargs)

        return results

    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        result = func(*args, **kwargs)
        name = func.__name__
        # print(name, args, now)
        print(f"func:{name} - args: {', '.join(map(str, args))} - [{now}] - Result: {result}")
        print(f"Result: {result}")

        return result

    return wrapper

@log_call
@validate_number
def multiply(a,b):
    return a*b

multiply(3,4)