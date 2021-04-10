from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_types = ('FreshwaterAquarium', 'SaltwaterAquarium')
        if aquarium_type not in valid_types:
            return 'Invalid aquarium type.'

        if aquarium_type == valid_types[0]:
            new_aquarium = FreshwaterAquarium(aquarium_name)
        else:
            new_aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(new_aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        valid_types = ('Ornament', 'Plant')
        if decoration_type not in valid_types:
            return 'Invalid decoration type.'

        if decoration_type == valid_types[0]:
            new_decoration = Ornament()
        else:
            new_decoration = Plant()

        self.decorations_repository.add(new_decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquariums = [a for a in self.aquariums if a.name == aquarium_name]

        if decoration == 'None':
            return f'There isn\'t a decoration of type {decoration_type}.'

        if not aquariums:
            return

        aquarium = aquariums[0]
        aquarium.add_decoration(decoration)
        is_removed = self.decorations_repository.remove(decoration)
        if is_removed:
            return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ('FreshwaterFish', 'SaltwaterFish')
        valid_aquarium_types = ('FreshwaterAquarium', 'SaltwaterAquarium')

        if fish_type not in valid_fish_types:
            return f'There isn\'t a fish of type {fish_type}.'

        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        if fish_type == valid_fish_types[0] and aquarium.__class__.__name__ == valid_aquarium_types[0]:
            new_fish = FreshwaterFish(name=fish_name, species=fish_species, price=price)
            return aquarium.add_fish(new_fish)
        elif fish_type == valid_fish_types[1] and aquarium.__class__.__name__ == valid_aquarium_types[1]:
            new_fish = SaltwaterFish(name=fish_name, species=fish_species, price=price)
            return aquarium.add_fish(new_fish)
        else:
            return 'Water not suitable.'

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        for fish in aquarium.fish:
            fish.eat()

        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        value = sum([d.price for d in aquarium.decorations]) + sum([f.price for f in aquarium.fish])
        return f'The value of Aquarium {aquarium_name} is {value:.2f}.'

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'

        return result[:-1]
