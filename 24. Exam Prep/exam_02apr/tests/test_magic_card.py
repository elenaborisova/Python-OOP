import unittest
from exam_02apr.project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):
    def test_magicCardInit_whenValidName_shouldSetIt(self):
        name = 'test'
        magic_card = MagicCard(name)

        self.assertEqual('test', magic_card.name)

    def test_magicCardInit_whenEmptyStringName_shouldRaise(self):
        name = ''

        with self.assertRaises(ValueError) as context:
            MagicCard(name)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's name cannot be an empty string.")

    def test_magicCardInit_shouldSetDamagePointsAndHealthPointsInInitialization(self):
        name = 'test'
        magic_card = MagicCard(name)

        self.assertEqual(5, magic_card.damage_points)
        self.assertEqual(80, magic_card.health_points)

    def test_magicCardInit_whenDamagePointsNegative_shouldRaise(self):
        name = 'test'
        magic_card = MagicCard(name)

        with self.assertRaises(ValueError) as context:
            magic_card.damage_points = -50

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's damage points cannot be less than zero.")

    def test_magicCardInit_whenHealthPointsNegative_shouldRaise(self):
        name = 'test'
        magic_card = MagicCard(name)

        with self.assertRaises(ValueError) as context:
            magic_card.health_points = -50

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Card's HP cannot be less than zero.")
