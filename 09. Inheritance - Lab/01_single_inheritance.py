class Animal:
    @staticmethod
    def eat():
        return "eating..."


class Dog(Animal):  # Single Inheritance
    @staticmethod
    def bark():
        return "barking..."


a = Animal()
print(a.eat())

dog = Dog()
print(dog.eat())
print(dog.bark())

