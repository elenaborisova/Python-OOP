from need_for_speed_04.project.car import Car


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = FamilyCar.DEFAULT_FUEL_CONSUMPTION
