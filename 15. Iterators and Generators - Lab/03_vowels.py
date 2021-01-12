class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowel_letters = ("a", "e", "i", "o", "u", "y")
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text) - 1:
            raise StopIteration()

        self.index += 1
        if self.text[self.index].lower() in self.vowel_letters:
            return self.text[self.index]
        return self.__next__()


my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)
