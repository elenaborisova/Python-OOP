from time import perf_counter


def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        return end_time - start_time
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


@exec_time
def concatenate(strings):
    result = ''
    for string in strings:
        result += string
    return result


print(loop(1, 10000000))
print(concatenate(['a' for i in range(10000000)]))

