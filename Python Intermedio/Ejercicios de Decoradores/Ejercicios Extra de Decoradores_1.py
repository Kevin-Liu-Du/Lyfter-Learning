def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat_twice
def to_greet(name):
    print(f"To greet: {name}")

to_greet("Kevin")