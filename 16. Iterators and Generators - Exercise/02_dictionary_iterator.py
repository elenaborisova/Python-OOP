from collections import deque


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = deque(self.dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.keys:
            raise StopIteration()

        key = self.keys.popleft()
        value = self.dictionary[key]
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
