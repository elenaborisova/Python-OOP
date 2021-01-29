import unittest
from unittest import TestCase
from test_person.person import Person


class TestPerson(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Executing setUpClass')

    def setUp(self) -> None:
        print('Executing')

    def test_valid_name_and_valid_age_should_return_correct_greeting(self):
        # Arrange
        name = 'Test user'
        age = 1
        expected = f'Hello! I am {name}, {age} years old.'
        p = Person(name, age)

        # Act
        actual = p.get_greeting()

        # Assert
        self.assertEqual(actual, expected)

    def test_invalid_name_should_raise_exception(self):
        name = None
        age = 1

        self.assertRaises(ValueError, lambda: Person(name, age))


if __name__ == '__main__':
    unittest.main()
