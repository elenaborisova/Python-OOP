from mix_it_06.project.capacity_mixin import CapacityMixin, CapacityReachedException


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots: int):
        self.parking_lots = parking_lots

    def check_availability(self):
        try:
            self.get_capacity(self.parking_lots, 1)
            self.parking_lots -= 1
            return f"Parking lots available: {self.parking_lots}"
        except CapacityReachedException:
            return "There are no more parking lots!"
