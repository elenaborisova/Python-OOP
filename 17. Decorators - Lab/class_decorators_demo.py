from functools import wraps
from time import sleep


def delay(seconds=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


class PrintPropertiesMixin:
    def __str__(self):
        pairs = [f"{key}={value}" for key, value in self.__dict__.items()]
        return "; ".join(pairs)


class Person(PrintPropertiesMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @delay(1)
    def __str__(self):
        return super().__str__()

    def __call__(self, *args, **kwargs):
        return f"From __call__: {self}"


p = Person("Elena", 23)
print(p)
print(p())


print = delay(2)(print)
print("Hello World")
