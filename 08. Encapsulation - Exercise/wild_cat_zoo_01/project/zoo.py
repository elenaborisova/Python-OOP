class Zoo:
    def __init__(self, name: str, budget: float, animal_capacity: int, workers_capacity: int):
        self.name: str = name
        self.animals: list = []
        self.workers: list = []

        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def have_budget_for_animals(self, price: float):
        return self.__budget >= price

    def get_tend_animals_cost(self):
        return sum([a.get_needs() for a in self.animals])

    def have_budget_to_tend_animals(self):
        return self.__budget >= self.get_tend_animals_cost()

    def have_animals_capacity(self):
        return self.__animal_capacity > len(self.animals)

    def get_salaries_sum(self):
        return sum([w.salary for w in self.workers])

    def have_budget_for_workers(self):
        return self.__budget >= self.get_salaries_sum()

    def have_workers_capacity(self):
        return self.__workers_capacity > len(self.workers)

    def add_animal(self, animal, price: float):
        if not self.have_animals_capacity():
            return "Not enough space for animal"
        if self.have_animals_capacity() and not self.have_budget_for_animals(price):
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.have_workers_capacity():
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        workers = [w for w in self.workers if w.name == worker_name]
        if not workers:
            return f"There is no {worker_name} in the zoo"

        worker = workers[0]
        self.workers.remove(worker)
        return f"{worker.name} fired successfully"

    def pay_workers(self):
        if not self.have_budget_for_workers():
            return "You have no budget to pay your workers. They are unhappy"

        salaries = self.get_salaries_sum()
        self.__budget -= salaries
        return f"You paid your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if not self.have_budget_to_tend_animals():
            return f"You have no budget to tend the animals. They are unhappy."

        tend_animals_cost = self.get_tend_animals_cost()
        self.__budget -= tend_animals_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: float):
        self.__budget += amount

    def get_animal_type(self, type_name: str):
        return [str(a) for a in self.animals if a.__class__.__name__ == type_name]

    def get_worker_type(self, type_name: str):
        return [str(w) for w in self.workers if w.__class__.__name__ == type_name]

    def animals_status(self):
        lions = self.get_animal_type("Lion")
        tigers = self.get_animal_type("Tiger")
        cheetahs = self.get_animal_type("Cheetah")
        new_line = "\n"

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n{new_line.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n{new_line.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n{new_line.join(cheetahs)}"

    def workers_status(self):
        keepers = self.get_worker_type("Keeper")
        caretakers = self.get_worker_type("Caretaker")
        vets = self.get_worker_type("Vet")
        new_line = "\n"

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n{new_line.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n{new_line.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n{new_line.join(vets)}"
