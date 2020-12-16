class Vet:
    animals = []
    SPACE = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: list = []

    def register_animal(self, animal_name: str):
        if len(Vet.animals) >= Vet.SPACE:
            return "Not enough space"
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        space_left = Vet.SPACE - len(Vet.animals)
        return f"{self.name} has {len(self.animals)} animals. " \
               f"{space_left} space left in clinic"


peter = Vet("Peter")
george = Vet("George")

print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))

print(peter.info())
print(george.info())