class PersonValidator:
    def is_valid(self, name, age):
        return name and 0 <= age <= 120


class Person:
    def __init__(self, name, age):
        self.__validator = PersonValidator()
        if not self.__validator.is_valid(name, age):
            raise Exception('Invalid person name or age')

        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # if value is None:
        #     raise ValueError('Name must be non-empty string!')
        self.__name = value

    def get_greeting(self):
        return f'Hello! I am {self.name}, {self.age} years old.'