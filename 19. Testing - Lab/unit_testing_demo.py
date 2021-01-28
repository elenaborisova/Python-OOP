def fail_if_different(value1, value2):
    if not value1 == value2:
        raise ValueError('Invalid test')


def add(x, y):
    return x + y


def test1():
    fail_if_different(
        add(1, 2),
        3
    )


def test2():
    fail_if_different(
        add(1, 1),
        2
    )


tests = [test1, test2]

[test() for test in tests]
