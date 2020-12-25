class CapacityReachedException(Exception):
    pass


class CapacityMixin:
    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            raise CapacityReachedException("Capacity reached!")
        return capacity - amount
