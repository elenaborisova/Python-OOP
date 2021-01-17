def uppercase_decorator(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


def lowercase_decorator(function):
    def wrapper():
        result = function()
        lowercase_result = result.lower()
        return lowercase_result

    return wrapper


def say_hi():
    return "Hello there!"


@uppercase_decorator
def say_bye():
    return f"Goodbye!"


@lowercase_decorator
@uppercase_decorator
def message():
    return "Some random message"


decorate = uppercase_decorator(say_hi)
print(decorate)

print(decorate())
print(say_bye())

print(message())
print(lowercase_decorator(uppercase_decorator(message))())
