from functools import wraps


def even_numbers(func):
    def is_even(number):
        return number % 2 == 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        return list(filter(is_even, numbers))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
