def print_decorators(func):
    def wrapper(*args, **kwargs):
        print(f"\n")
        print("args:", args)
        print("kwargs:", kwargs)

        results = func(*args, **kwargs)

        print(f"return:", results)

        return results

    return wrapper


@print_decorators
def sum(a, b):
    return a + b
sum(2, 3)

@print_decorators
def sum(a=6, b=3):
    return a + b
sum()

@print_decorators
def sum(a, b):
    return a * b
sum(6, 3)

@print_decorators
def sum(a=2, b=2):
    return a + b
sum(1, 1)

