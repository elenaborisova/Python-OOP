from functools import wraps
from time import sleep

LOGGER_TYPES = {"file": "file", "cmd": "cmd"}


def log(type=LOGGER_TYPES["cmd"]):
    def print_to_cmd(text):
        print(text)

    def print_to_file(text):
        with open("log.txt", "a") as file:
            file.write(text)
            file.write("\n")

    def decorator(func):
        print_func = print_to_cmd
        if type == LOGGER_TYPES["file"]:
            print_func = print_to_file

        @wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(map(str, args))
            print_func(f"--- Executing {func.__name__}({args_str}) ---")
            func(*args, **kwargs)

        return wrapper

    return decorator


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


def delay(seconds=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(4)
@delay(1)
@log()
def say_hello(name):
    print(f"Hello, {name}")


@repeat(4)
@delay()
def say_hi():
    print("Hello")


say_hello("Elena")
say_hi()
