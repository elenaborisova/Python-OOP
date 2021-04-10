import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):
    def test_init_shouldInitialize(self):
        train = Train('test name', 100)

        self.assertEqual('test name', train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_whenValid_shouldAddPassengerToPassengersList(self):
        train = Train('test name', 100)

        result = train.add('passenger test name')

        self.assertEqual(['passenger test name'], train.passengers)
        self.assertEqual('Added passenger passenger test name', result)

    def test_add_whenNotEnoughCapacity_shouldRaise(self):
        train = Train('test name', 1)
        train.add('passenger test name')

        with self.assertRaises(ValueError) as context:
            train.add('passenger test name2')

        self.assertIsNotNone(context.exception)

    def test_add_whenPassengerNameAlreadyExists_shouldRaise(self):
        train = Train('test name', 100)
        train.add('passenger test name')

        with self.assertRaises(ValueError) as context:
            train.add('passenger test name')

        self.assertIsNotNone(context.exception)

    def test_remove_whenValid_shouldRemovePassenger(self):
        train = Train('test name', 100)
        train.add('passenger test name')

        result = train.remove('passenger test name')

        self.assertEqual([], train.passengers)
        self.assertEqual('Removed passenger test name', result)

    def test_remove_whenPassengerNonExistent_shouldRaise(self):
        train = Train('test name', 100)

        with self.assertRaises(ValueError) as context:
            train.remove('passenger test name')

        self.assertIsNotNone(context.exception)
