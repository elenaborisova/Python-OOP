class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: list = []

    def __repr__(self):
        dvd_names = ", ".join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} " \
               f"has {len(self.rented_dvds)} rented DVD's ({dvd_names})"
