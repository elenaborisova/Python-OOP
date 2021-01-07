from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound = "meow"

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.sound = "woof-woof"

    def make_sound(self):
        return self.sound + " showing teeth"


animals = [Dog(), Cat()]
for a in animals:
    print(a.make_sound())
