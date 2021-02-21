from errors import CustomListIndexException, CustomListTypeException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListRemoveTests(CustomListTestBase):
    def test_customListRemove_whenIndexInTheMiddle_shouldRemoveAndReturnElementAtIndex(self):
        index = 2

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.remove(index)

        self.assertListEqual([1, 2, 4], custom_list.data)
        self.assertEqual(3, result)

    def test_customListRemove_whenIndexIs0_shouldRemoveAndReturnFirstElement(self):
        index = 0

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.remove(index)

        self.assertListEqual([2, 3, 4], custom_list.data)
        self.assertEqual(1, result)

    def test_customListRemove_whenIndexIsLast_shouldRemoveAndReturnLastElement(self):
        index = 3

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.remove(index)

        self.assertListEqual([1, 2, 3], custom_list.data)
        self.assertEqual(4, result)

    def test_customListRemove_whenListHasSingleElement_shouldRemoveAndReturnIt(self):
        index = 0

        custom_list = self.setup_list(1)
        result = custom_list.remove(index)

        self.assertListEqual([], custom_list.data)
        self.assertEqual(1, result)

    def test_customListRemove_whenIndexIsEqualToLen_shouldRaise(self):
        list_len = 4
        custom_list = self.setup_list(range(list_len))

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.remove(list_len)

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsLessThanNegativeLen_shouldRaise(self):
        list_len = 4
        custom_list = self.setup_list(range(list_len))

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.remove(-list_len - 1)

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsNotInt_shouldRaise(self):
        index = "abc"
        custom_list = self.setup_list(1, 2, 3, 4)

        with self.assertRaises(CustomListTypeException) as context:
            custom_list.remove(index)

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenListIsEmpty_shouldRaise(self):
        index = 0
        custom_list = self.setup_list()

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.remove(index)

        self.assertIsNotNone(context.exception)
