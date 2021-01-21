def adder():
    i = 0

    def add():
        nonlocal i
        i += 1

    def get():
        return i

    return add, get


def exec(fn):
    return fn()


add, get = adder()
add()
add()
add()
print(get())
