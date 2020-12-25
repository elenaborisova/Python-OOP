from need_for_speed_04.project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
