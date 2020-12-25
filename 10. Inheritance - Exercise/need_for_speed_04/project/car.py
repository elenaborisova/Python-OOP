from need_for_speed_04.project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION: float = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = Car.DEFAULT_FUEL_CONSUMPTION
