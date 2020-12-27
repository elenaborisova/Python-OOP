from need_for_speed_04.project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = SportCar.DEFAULT_FUEL_CONSUMPTION
