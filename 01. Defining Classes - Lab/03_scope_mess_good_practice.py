x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        return "global: changed!"

    print("outer:", x)
    x = inner()
    print("outer:", x)

    return change_global()


print(x)
x = outer()
print(x)