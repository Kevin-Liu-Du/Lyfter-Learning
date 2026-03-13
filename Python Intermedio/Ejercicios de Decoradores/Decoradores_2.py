def check_int(func):
    def wrapper(*args, **kwargs):
        for argument in args:
            if not isinstance(argument, int):
                    raise TypeError("Error, must be a number format. ")

        for value in kwargs.values():
            if not isinstance(value, int):
                    raise TypeError("Error, must be a number format. ")

        results = func(*args, **kwargs)

        return results

    return wrapper


@check_int
def sum(a, b):
    return a + b

sum(5, 3.2)