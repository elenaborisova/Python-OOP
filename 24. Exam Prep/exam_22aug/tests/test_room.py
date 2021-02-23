import unittest
from exam_22aug.project.people.child import Child
from exam_22aug.project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def test_roomInit_shouldHaveAllAttributes(self):
        room = Room('Test name', 100, 2)

        self.assertEqual('Test name', room.family_name)
        self.assertEqual(100, room.budget)
        self.assertEqual(2, room.members_count)
        self.assertListEqual([], room.children)
        self.assertEqual(0, room.expenses)

    def test_roomPropertyExpensesSetter_whenValueIsMoreThanZero_shouldSetExpensesToValue(self):
        room = Room('Test name', 100, 2)

        room.expenses = 50
        self.assertEqual(50, room.expenses)

    def test_roomPropertyExpensesSetter_whenValueIsLessOrEqualToZero_shouldRaise(self):
        room = Room('Test name', 100, 2)

        with self.assertRaises(ValueError) as context:
            room.expenses = -50

        self.assertIsNotNone(context.exception)

    def test_roomCalculateExpenses_whenPassedChildrenList_shouldCalculateAndReturnExpenses(self):
        room = Room('Test name', 100, 2)
        child1 = Child(1, 2)
        child2 = Child(2, 3)
        room.children = [child1, child2]

        result = room.calculate_expenses(room.children)

        self.assertEqual(90 + 150, result)

    def test_roomCalculateExpenses_whenNotPassedAnything_shouldCalculateAndReturnZeroExpenses(self):
        room = Room('Test name', 100, 2)

        result = room.calculate_expenses(room.children)

        self.assertEqual(0, result)
