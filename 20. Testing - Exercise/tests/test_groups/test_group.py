import unittest
from groups import Person, Group


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('Elena', 'Borisova')
        self.person_2 = Person('John', 'Smith')
        self.name = 'test'
        self.people = [self.person_1, self.person_2]
        self.group = Group(self.name, self.people)

    def test_groupLen_shouldReturnTheLengthOfPeople(self):
        actual = len(self.group)
        expected = len(self.group.people)

        self.assertEqual(actual, expected)

    def test_groupAdd_shouldReturnNewGroupWithAllPeople(self):
        person_3 = Person('George', 'Francis')
        group_2 = Group('test2', [person_3])

        new_group = self.group + group_2

        self.assertEqual(new_group.people, [self.person_1, self.person_2, person_3])
        self.assertEqual(new_group.name, 'test')

    def test_groupGetItem_whenValidIndex_shouldReturnAStringWithIndexAndPerson(self):
        actual = self.group[0]
        expected = f"Person 0: Elena Borisova"

        self.assertEqual(actual, expected)

    def test_groupGetItem_whenInvalidIndex_shouldRaise(self):
        with self.assertRaises(IndexError) as context:
            self.group[5]

        self.assertIsNotNone(context.exception)

    def test_groupRepr_shouldReturnString(self):
        actual = repr(self.group)
        expected = f"Group test with members Elena Borisova, John Smith"

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
