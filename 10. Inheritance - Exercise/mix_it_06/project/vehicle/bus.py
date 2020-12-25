from mix_it_06.project.capacity_mixin import CapacityReachedException
from mix_it_06.project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats: int, ticket_price: float):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold: int = 0

    def get_ticket(self, ticket_count: int):
        try:
            self.get_capacity(self.available_seats, ticket_count)
            self.tickets_sold += ticket_count
            self.available_seats -= ticket_count
        except CapacityReachedException as ex:
            return str(ex)

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price
