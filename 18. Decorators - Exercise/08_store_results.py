class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open('results.txt', 'a') as file:
            file.write(f"Function '{self.func.__name__}' was called. "
                       f"Result: {self.func(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def multiply(a, b):
    return a * b


add(2, 2)
multiply(6, 4)
