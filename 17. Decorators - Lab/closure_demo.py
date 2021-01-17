def get_summator():
    result = 0

    def add(x):
        nonlocal result
        result += x
        return result

    return add


summator = get_summator()
summator2 = get_summator()

print(summator(1))
print(summator(1))
print(summator(1))
print(summator(1))
print(summator2(1))
print(summator(1))
