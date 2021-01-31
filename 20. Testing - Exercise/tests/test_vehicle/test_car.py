import unittest
from vehicle import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.fuel_quantity = 100
        self.fuel_consumption = 3
        self.car = Car(self.fuel_quantity, self.fuel_consumption)

    def test_carDrive_whenNotEnoughFuel(self):
        distance = 40
        self.car.drive(distance)

        self.assertEqual(self.fuel_quantity, self.car.fuel_quantity)

    def test_carDrive_whenEnoughFuel(self):
        distance = 10
        self.car.drive(distance)

        expected = self.fuel_quantity - (self.car.fuel_consumption + self.car.INCREASED_CONSUMPTION) * distance
        self.assertEqual(expected, self.car.fuel_quantity)

    def test_carRefuel_shouldIncreaseFuelQuantity(self):
        amount = 10
        self.car.refuel(amount)

        self.assertEqual(self.fuel_quantity + amount, self.car.fuel_quantity)


if __name__ == '__main__':
    unittest.main()
