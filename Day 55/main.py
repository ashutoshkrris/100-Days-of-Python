def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
