from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        start_time = timer()
        func(*args)
        end_time = timer()
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


print(loop(1, 10))
print(concatenate(['a' for i in range(10)]))

