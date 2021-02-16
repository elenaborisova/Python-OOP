from errors import CustomListIndexException, CustomListTypeException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListGetTests(CustomListTestBase):
    def test_customListGet_whenIndexInTheMiddle_shouldReturnElementAtIndex(self):
        index = 2

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.get(index)

        self.assertEqual(3, result)

    def test_customListGet_whenIndexIs0_shouldReturnFirstElement(self):
        index = 0

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.get(index)

        self.assertEqual(1, result)

    def test_customListGet_whenIndexIsLast_shouldReturnLastElement(self):
        index = 3

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.get(index)

        self.assertEqual(4, result)

    def test_customListGet_whenListHasSingleElement_shouldReturnIt(self):
        index = 0

        custom_list = self.setup_list(1)
        result = custom_list.get(index)

        self.assertEqual(1, result)

    def test_customListGet_whenIndexIsEqualToLen_shouldRaise(self):
        list_len = 4
        custom_list = self.setup_list(range(list_len))

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.get(list_len)

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsLessThanNegativeLen_shouldRaise(self):
        list_len = 4
        custom_list = self.setup_list(range(list_len))

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.get(-list_len - 1)

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsNotInt_shouldRaise(self):
        index = "abc"
        custom_list = self.setup_list(1, 2, 3, 4)

        with self.assertRaises(CustomListTypeException) as context:
            custom_list.get(index)

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenListIsEmpty_shouldRaise(self):
        index = 0
        custom_list = self.setup_list()

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.get(index)

        self.assertIsNotNone(context.exception)
