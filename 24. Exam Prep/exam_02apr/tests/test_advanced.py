import unittest
from exam_02apr.project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def test_advancedInit_whenValidUsername_shouldIt(self):
        username = 'test'
        advanced_p = Advanced(username)

        self.assertEqual('test', advanced_p.username)

    def test_advancedInit_whenEmptyStringUsername_shouldRaise(self):
        username = ''

        with self.assertRaises(ValueError) as context:
            Advanced(username)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Player's username cannot be an empty string.")

    def test_advancedInit_shouldSetHealthTo250(self):
        username = 'test'
        advanced_p = Advanced(username)

        self.assertEqual(250, advanced_p.health)

    def test_advancedInit_whenSetHealthToNegative_shouldRaise(self):
        username = 'test'
        advanced_p = Advanced(username)

        with self.assertRaises(ValueError) as context:
            advanced_p.health = -250

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_advancedInit_shouldInitializeCardRepository(self):
        username = 'test'
        advanced_p = Advanced(username)

        self.assertEqual('CardRepository', advanced_p.card_repository.__class__.__name__)

    def test_advancedInit_whenPositiveHealth_shouldSetIsDeadPropertyToFalse(self):
        username = 'test'
        advanced_p = Advanced(username)

        self.assertFalse(advanced_p.is_dead)

    def test_advancedInit_whenZeroHealth_shouldSetIsDeadPropertyToTrue(self):
        username = 'test'
        advanced_p = Advanced(username)
        advanced_p.health = 0

        self.assertTrue(advanced_p.is_dead)

    def test_advancedTakeDamage_whenPositiveDamagePoints_shouldReduceHealth(self):
        username = 'test'
        advanced_p = Advanced(username)
        advanced_p.take_damage(50)

        self.assertEqual(200, advanced_p.health)

    def test_advancedTakeDamage_whenZeroDamagePoints_shouldReduceHealth(self):
        username = 'test'
        advanced_p = Advanced(username)
        advanced_p.take_damage(0)

        self.assertEqual(250, advanced_p.health)

    def test_advancedTakeDamage_whenNegativeDamagePoints_shouldRaise(self):
        username = 'test'
        advanced_p = Advanced(username)

        with self.assertRaises(ValueError) as context:
            advanced_p.take_damage(-50)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Damage points cannot be less than zero.')
