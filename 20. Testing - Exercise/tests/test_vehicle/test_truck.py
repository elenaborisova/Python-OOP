import unittest
from vehicle import Truck


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.fuel_quantity = 100
        self.fuel_consumption = 3
        self.truck = Truck(self.fuel_quantity, self.fuel_consumption)

    def test_carDrive_whenNotEnoughFuel(self):
        distance = 40
        self.truck.drive(distance)

        self.assertEqual(self.fuel_quantity, self.truck.fuel_quantity)

    def test_carDrive_whenEnoughFuel(self):
        distance = 10
        self.truck.drive(distance)

        expected = self.fuel_quantity - (self.truck.fuel_consumption + self.truck.INCREASED_CONSUMPTION) * distance
        self.assertEqual(expected, self.truck.fuel_quantity)

    def test_carRefuel_shouldIncreaseFuelQuantity(self):
        amount = 10
        self.truck.refuel(amount)

        self.assertEqual(self.fuel_quantity + (amount * 0.95), self.truck.fuel_quantity)


if __name__ == '__main__':
    unittest.main()
