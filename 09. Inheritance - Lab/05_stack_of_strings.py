class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)


ss = Stack()
ss.push(10)
ss.push(43)
ss.push(24)

print(ss.is_empty())
print(ss)
