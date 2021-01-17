from time import perf_counter


def measure(func, *args):
    start_time = perf_counter()
    result = func(*args)
    end_time = perf_counter()
    execution_time = end_time - start_time
    print(f"Function executed for {execution_time} seconds")
    return result
