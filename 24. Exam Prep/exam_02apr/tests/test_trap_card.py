import unittest
from exam_02apr.project.card.trap_card import TrapCard


class TrapCardTests(unittest.TestCase):
    def test_trapCardInit_whenValidName_shouldSetIt(self):
        name = 'test'
        trap_card = TrapCard(name)

        self.assertEqual('test', trap_card.name)

    def test_trapCardInit_whenEmptyStringName_shouldRaise(self):
        name = ''

        with self.assertRaises(ValueError) as context:
            TrapCard(name)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's name cannot be an empty string.")

    def test_trapCardInit_shouldSetDamagePointsAndHealthPointsInInitialization(self):
        name = 'test'
        trap_card = TrapCard(name)

        self.assertEqual(120, trap_card.damage_points)
        self.assertEqual(5, trap_card.health_points)

    def test_trapCardInit_whenDamagePointsNegative_shouldRaise(self):
        name = 'test'
        trap_card = TrapCard(name)

        with self.assertRaises(ValueError) as context:
            trap_card.damage_points = -50

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's damage points cannot be less than zero.")

    def test_trapCardInit_whenHealthPointsNegative_shouldRaise(self):
        name = 'test'
        trap_card = TrapCard(name)

        with self.assertRaises(ValueError) as context:
            trap_card.health_points = -50

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's HP cannot be less than zero.")
