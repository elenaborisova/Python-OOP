from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Aquarium name cannot be an empty string.')
        self._name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if self.capacity <= len(self.fish):
            return 'Not enough capacity.'

        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names_str = " ".join([fish.name for fish in self.fish])

        return f'{self.name}:\n' \
               f'Fish: {fish_names_str if self.fish else "none"}\n' \
               f'Decorations: {len(self.decorations)}\n' \
               f'Comfort: {self.calculate_comfort()}'
