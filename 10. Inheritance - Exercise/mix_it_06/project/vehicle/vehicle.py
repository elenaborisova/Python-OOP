from mix_it_06.project.capacity_mixin import CapacityMixin


class Vehicle(CapacityMixin):
    def __init__(self, available_seat: int):
        self.available_seats = available_seat
