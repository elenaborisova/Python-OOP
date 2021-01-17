def execute_func(func, *args, **kwargs):
    print(f" --- Before {func.__name__}() ---")
    result = func(*args, **kwargs)
    print(f" --- After {func.__name__}() ---")
    return result


def choose_operation(operation):
    def sum_numbers(*args):
        return sum(args)

    def multiply_numbers(*args):
        pass

    if operation == "+":
        return sum_numbers
    else:
        return multiply_numbers


execute_func(print, "Hello")

operation_func1 = choose_operation("+")
operation_func2 = choose_operation("*")

print(operation_func1(1, 2, 4))
print(operation_func2(1, 2, 4))

print(execute_func(choose_operation("+"), 1, 2, 4))
