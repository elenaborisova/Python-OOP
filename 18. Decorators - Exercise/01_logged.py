def logged(fn):
    def wrapper(*args, **kwargs):
        message = f"you called {fn.__name__}{args}\n"
        fn_result = f"it returned {fn(*args, **kwargs)}"
        return message + fn_result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
