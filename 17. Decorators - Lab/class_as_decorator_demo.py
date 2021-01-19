from time import sleep


class delay_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        sleep(2)
        result = self.func(*args, **kwargs)
        return result


@delay_decorator
def say_hi(name):
    return f"Hi, {name}!"


print(say_hi("Elena"))
