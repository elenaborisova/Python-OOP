def validate_numbers(args):
    return all(isinstance(a, int) for a in args)


def even_parameters(func):
    def wrapper(*args, **kwargs):
        if validate_numbers(args) and all(a % 2 == 0 for a in args):
            return func(*args, **kwargs)
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add('Peter', 1))

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
