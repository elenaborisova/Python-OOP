from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.INCREASED_CONSUMPTION = 0.9

    def get_fuel_needed(self, distance):
        return (self.fuel_consumption + self.INCREASED_CONSUMPTION) * distance

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.INCREASED_CONSUMPTION = 1.6

    def get_fuel_needed(self, distance):
        return (self.fuel_consumption + self.INCREASED_CONSUMPTION) * distance

    def drive(self, distance):
        fuel_needed = self.get_fuel_needed(distance)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
