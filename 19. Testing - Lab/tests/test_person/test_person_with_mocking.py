from unittest import TestCase, mock
from mocking_demo import Person


class TestPerson(TestCase):
    def test_personGetGreeting_shouldReturnCorrectGreeting(self):
        with mock.patch('mocking_demo.PersonValidator') as MockPersonValidator:
            MockPersonValidator.return_value.is_valid.return_value = True

            Person(None, -1)
