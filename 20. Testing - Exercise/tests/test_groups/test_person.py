import unittest
from groups import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.name = 'test name'
        self.surname = 'test surname'

        self.person_1 = Person(self.name, self.surname)

    def test_personRepr_shouldReturnString(self):
        actual = repr(self.person_1)
        expected = f"Person {self.person_1.id}: test name test surname"

        self.assertEqual(actual, expected)

    def test_personStr_shouldConcatenateNameAndSurname(self):
        actual = str(self.person_1)
        expected = 'test name test surname'

        self.assertEqual(actual, expected)

    def test_personAutoIncrementId(self):
        person_2 = Person('test name 2', 'test surname 2')

        self.assertEqual(self.person_1.id, 3)
        self.assertEqual(person_2.id, 4)
        self.assertEqual(Person.id_counter, 5)

    def test_personAdd_shouldReturnNewInstanceWithFirstNameAndSecondSurname(self):
        person_2 = Person('test name 2', 'test surname 2')

        new_person = self.person_1 + person_2

        self.assertEqual(new_person.name, self.person_1.name)
        self.assertEqual(new_person.surname, person_2.surname)


if __name__ == '__main__':
    unittest.main()
