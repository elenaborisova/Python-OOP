class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError('Name must be non-empty string')
        self.__name = value

    def get_greeting(self):
        return f'Hello! I am {self.name}, {self.age} years old.'
