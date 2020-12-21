from wild_cat_zoo_01.project.caretaker import Caretaker
from wild_cat_zoo_01.project.cheetah import Cheetah
from wild_cat_zoo_01.project.keeper import Keeper
from wild_cat_zoo_01.project.lion import Lion
from wild_cat_zoo_01.project.tiger import Tiger
from wild_cat_zoo_01.project.vet import Vet
from wild_cat_zoo_01.project.zoo import Zoo


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animal Creation
animals = [
    Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),
    Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3),
    Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4),
]

# Animal Prices
prices = [200, 190, 204, 156, 211, 140]

# Workers Creation
workers = [
    Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95),
    Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),
    Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)
]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Firing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
