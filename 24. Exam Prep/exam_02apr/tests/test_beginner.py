import unittest
from exam_02apr.project.player.beginner import Beginner


class BeginnerTests(unittest.TestCase):
    def test_BeginnerInit_whenValidUsername_shouldIt(self):
        username = 'test'
        beginner_p = Beginner(username)

        self.assertEqual('test', beginner_p.username)

    def test_BeginnerInit_whenEmptyStringUsername_shouldRaise(self):
        username = ''

        with self.assertRaises(ValueError) as context:
            Beginner(username)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Player's username cannot be an empty string.")

    def test_BeginnerInit_shouldSetHealthTo50(self):
        username = 'test'
        beginner_p = Beginner(username)

        self.assertEqual(50, beginner_p.health)

    def test_BeginnerInit_whenSetHealthToNegative_shouldRaise(self):
        username = 'test'
        beginner_p = Beginner(username)

        with self.assertRaises(ValueError) as context:
            beginner_p.health = -250

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_BeginnerInit_shouldInitializeCardRepository(self):
        username = 'test'
        beginner_p = Beginner(username)

        self.assertEqual('CardRepository', beginner_p.card_repository.__class__.__name__)

    def test_beginnerInit_whenPositiveHealth_shouldSetIsDeadPropertyToFalse(self):
        username = 'test'
        beginner_p = Beginner(username)

        self.assertFalse(beginner_p.is_dead)

    def test_beginnerInit_whenZeroHealth_shouldSetIsDeadPropertyToTrue(self):
        username = 'test'
        beginner_p = Beginner(username)
        beginner_p.health = 0

        self.assertTrue(beginner_p.is_dead)

    def test_beginnerTakeDamage_whenPositiveDamagePoints_shouldReduceHealth(self):
        username = 'test'
        beginner_p = Beginner(username)
        beginner_p.take_damage(20)

        self.assertEqual(30, beginner_p.health)

    def test_beginnerTakeDamage_whenZeroDamagePoints_shouldReduceHealth(self):
        username = 'test'
        beginner_p = Beginner(username)
        beginner_p.take_damage(0)

        self.assertEqual(50, beginner_p.health)

    def test_beginnerTakeDamage_whenNegativeDamagePoints_shouldRaise(self):
        username = 'test'
        beginner_p = Beginner(username)

        with self.assertRaises(ValueError) as context:
            beginner_p.take_damage(-50)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Damage points cannot be less than zero.')
