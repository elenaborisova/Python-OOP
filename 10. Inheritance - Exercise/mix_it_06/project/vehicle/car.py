from mix_it_06.project.capacity_mixin import CapacityReachedException
from mix_it_06.project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value <= self.fuel_tank:
            self.__fuel = value

    def have_enough_fuel(self, fuel_needed: float):
        return self.fuel >= fuel_needed

    def drive(self, distance: float):
        fuel_needed = self.fuel_consumption * distance
        if self.have_enough_fuel(fuel_needed):
            self.fuel -= fuel_needed
            return "We've enjoyed the travel!"

    def refuel(self, liters: float):
        try:
            self.get_capacity(self.fuel_tank, liters + self.fuel)
            self.fuel += liters
            return self.fuel
        except CapacityReachedException as ex:
            return str(ex)

