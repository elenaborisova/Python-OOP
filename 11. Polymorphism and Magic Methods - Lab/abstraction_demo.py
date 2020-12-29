from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def sound(self):
        print("Bark")


dog = Dog("Sharo", 5)
dog.sound()
