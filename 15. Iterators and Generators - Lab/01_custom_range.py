class custom_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.increment = 1

        if self.step < 0:
            self.start, self.end = self.end, self.start
            self.increment = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment > 0:
            if self.start > self.end:
                raise StopIteration()
        else:
            if self.start < self.end:
                raise StopIteration()

        temp = self.start
        self.start += self.step
        return temp


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
