from mix_it_06.project.technology.technology import Technology
from mix_it_06.project.capacity_mixin import CapacityReachedException


class SmartPhone(Technology):
    def install_apps(self, app: str, app_memory: float):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken + app_memory)
            self.memory_taken += app_memory
            return memory_left
        except CapacityReachedException:
            return f"You don't have enough space for {app}!"
