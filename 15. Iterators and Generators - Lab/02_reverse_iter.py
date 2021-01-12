class reverse_iter:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= -len(self.sequence):
            raise StopIteration()

        self.index -= 1
        return self.sequence[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
