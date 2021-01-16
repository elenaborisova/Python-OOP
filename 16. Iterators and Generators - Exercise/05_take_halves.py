def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        take_list = []
        for num in seq:
            if len(take_list) == n:
                return take_list
            take_list.append(num)

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
