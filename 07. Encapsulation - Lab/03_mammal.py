class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type: str, sound: str):
        self.name = name
        self.type = type
        self.sound = sound

    @classmethod
    def get_kingdom(cls):
        return cls.__kingdom

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

