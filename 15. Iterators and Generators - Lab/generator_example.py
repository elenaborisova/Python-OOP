def my_gen():
    n = 1
    print("This is printed first")
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed last")
    yield n


print(list(my_gen()))
