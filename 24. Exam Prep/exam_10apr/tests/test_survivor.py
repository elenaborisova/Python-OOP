import unittest
from exam_10apr.project.survivor import Survivor


class SurvivorTests(unittest.TestCase):
    def test_survivorInit_whenNameIsValid_shouldAssignIt(self):
        survivor = Survivor('test', 23)
        self.assertEqual('test', survivor.name)

    def test_survivorInit_whenNameIsInvalid_shouldRaise(self):
        with self.assertRaises(ValueError) as context:
            Survivor('', 23)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Name not valid!')

    def test_survivorInit_whenAgeIsValid_shouldAssignIt(self):
        survivor = Survivor('test', 23)
        self.assertEqual(23, survivor.age)

    def test_survivorInit_whenAgeIsInvalid_shouldRaise(self):
        with self.assertRaises(ValueError) as context:
            Survivor('test', -23)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Age not valid!')

    def test_survivorInit_whenHealthIsValid_shouldAssignIt(self):
        survivor = Survivor('test', 23)
        survivor.health = 50

        self.assertEqual(50, survivor.health)

    def test_survivorInit_whenHealthIsGreaterThan100_shouldSetTo100(self):
        survivor = Survivor('test', 23)
        survivor.health = 150

        self.assertEqual(100, survivor.health)

    def test_survivorInit_whenHealthIsInvalid_shouldRaise(self):
        survivor = Survivor('test', 23)

        with self.assertRaises(ValueError) as context:
            survivor.health = -100

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Health not valid!')

    def test_survivorInit_whenNeedsIsValid_shouldAssignIt(self):
        survivor = Survivor('test', 23)
        survivor.needs = 50

        self.assertEqual(50, survivor.needs)

    def test_survivorInit_whenNeedsIsGreaterThan100_shouldSetTo100(self):
        survivor = Survivor('test', 23)
        survivor.needs = 150

        self.assertEqual(100, survivor.needs)

    def test_survivorInit_whenNeedsIsInvalid_shouldRaise(self):
        survivor = Survivor('test', 23)

        with self.assertRaises(ValueError) as context:
            survivor.needs = -100

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Needs not valid!')

    def test_survivorNeedsSustenance_whenNeedsLessThan100_shouldReturnTrue(self):
        survivor = Survivor('test', 23)
        survivor.needs = 50

        self.assertTrue(survivor.needs_sustenance)

    def test_survivorNeedsSustenance_whenNeedsMoreOrEqualTo100_shouldReturnFalse(self):
        survivor = Survivor('test', 23)

        self.assertFalse(survivor.needs_sustenance)

    def test_survivorNeedsHealing_whenHealthLessThan100_shouldReturnTrue(self):
        survivor = Survivor('test', 23)
        survivor.health = 50

        self.assertTrue(survivor.needs_healing)

    def test_survivorNeedsHealing_whenHealthMoreOrEqualTo100_shouldReturnFalse(self):
        survivor = Survivor('test', 23)

        self.assertFalse(survivor.needs_healing)


if __name__ == '__main__':
    unittest.main()
