from mix_it_06.project.capacity_mixin import CapacityReachedException
from mix_it_06.project.technology.technology import Technology


class Laptop(Technology):
    def install_software(self, software: str, software_memory: float):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken + software_memory)
            self.memory_taken += software_memory
            return memory_left
        except CapacityReachedException:
            return f"You don't have enough space for {software}!"
