import unittest
from list_03.integer_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def _test_integerListInit_whenNotOnlyIntegers_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, True, 5)

        self.assertIsNotNone(context.exception)

    def test_integerListInit_whenOnlyIntegers_shouldStoreThem(self):
        values = [1, 2, 3, 4, 5]
        il = IntegerList(*values)

        self.assertListEqual(values, il.data)

    def test_integerListAdd_whenValueIsInteger_shouldBeAdded(self):
        il = IntegerList()
        il.add(1)

        self.assertListEqual([1], il.data)

    def test_integerListAdd_whenValueNotInteger_shouldRaiseException(self):
        il = IntegerList()

        with self.assertRaises(Exception) as context:
            il.add({})

        self.assertIsNotNone(context.exception)

    def test_integerListRemoveIndex_whenIndexIsValid_shouldRemoveAndReturnElement(self):
        il = IntegerList(1, 2, 3, 4, 5)
        returned = il.remove_index(3)

        self.assertListEqual([1, 2, 3, 5], il.data)
        self.assertEqual(4, returned)

    def test_integerListRemoveIndex_whenIndexIsInvalid_shouldRaiseException(self):
        il = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            il.remove_index(len(il.data))

        self.assertIsNotNone(context.exception)

    def test_integerListGet_whenIndexIsValid_shouldReturnElement(self):
        il = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(1, il.get(0))

    def test_integerListGet_whenIndexIsInvalid_shouldRaiseException(self):
        il = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            il.get(len(il.data))

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenIndexIsValid_shouldInsertIt(self):
        il = IntegerList(1, 2, 3, 4, 5)

        il.insert(0, 0)
        self.assertEqual(0, il.data[0])

    def test_integerListInsert_whenIndexIsInvalid_shouldRaiseException(self):
        il = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            il.insert(15, 0)

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenElementIsInteger_shouldInsertIt(self):
        il = IntegerList(1, 2, 3, 4, 5)

        il.insert(0, 0)
        self.assertEqual(0, il.data[0])

    def test_integerListInsert_whenElementIsNotInteger_shouldRaiseException(self):
        il = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            il.insert(0, "invalid")

        self.assertIsNotNone(context.exception)

    def test_integerListGetBiggest_shouldReturnBiggestElement(self):
        il = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(5, il.get_biggest())

    def test_integerListGetIndex_shouldReturnElementIndex(self):
        il = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(0, il.get_index(1))


if __name__ == '__main__':
    unittest.main()
