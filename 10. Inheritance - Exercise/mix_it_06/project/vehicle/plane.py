from mix_it_06.project.capacity_mixin import CapacityReachedException
from mix_it_06.project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats: int, rows: int, seats_per_row: int):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available: dict = {row: self.seats_per_row for row in range(1, rows + 1)}

    def is_row_valid(self, row_number: int):
        return row_number in self.seats_available

    def buy_tickets(self, row_number: int, tickets_count: int):
        if not self.is_row_valid(row_number):
            return f"There is no row {row_number} in the plane!"

        available_seats_on_row = self.seats_available[row_number]
        try:
            self.get_capacity(available_seats_on_row, tickets_count)
            self.seats_available[row_number] -= tickets_count
            self.available_seats -= tickets_count
            return tickets_count
        except CapacityReachedException:
            return f"Not enough tickets on row {row_number}!"
