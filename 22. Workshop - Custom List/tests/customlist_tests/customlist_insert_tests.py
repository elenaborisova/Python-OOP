from errors import CustomListTypeException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListInsertTests(CustomListTestBase):
    def test_customListInsert_whenIndexInTheMiddle_shouldInsertElementAndReturnList(self):
        index = 2
        value = 2

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.insert(index, value)

        self.assertListEqual([1, 2, 2, 3, 4], custom_list.data)
        self.assertEqual([1, 2, 2, 3, 4], result)

    def test_customListInsert_whenIndexIs0_shouldInsertElementAndReturnList(self):
        index = 0
        value = 0

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.insert(index, value)

        self.assertListEqual([0, 1, 2, 3, 4], custom_list.data)
        self.assertEqual([0, 1, 2, 3, 4], result)

    def test_customListInsert_whenListHasSingleElement_shouldInsertElementAndReturnList(self):
        index = 0
        value = 0

        custom_list = self.setup_list(1)
        result = custom_list.insert(index, value)

        self.assertListEqual([0, 1], custom_list.data)
        self.assertEqual([0, 1], result)

    def test_customListInsert_whenIndexIsEqualToLen_shouldInsertElementAndReturnList(self):
        list_len = 4
        value = 4

        custom_list = self.setup_list(0, 1, 2, 3)
        result = custom_list.insert(list_len, value)

        self.assertListEqual([0, 1, 2, 3, 4], custom_list.data)
        self.assertEqual([0, 1, 2, 3, 4], result)

    def test_customListInsert_whenListIsEmptyAndInsertAt0_shouldInsertElementAndReturnList(self):
        index = 0
        value = 0

        custom_list = self.setup_list()
        result = custom_list.insert(index, value)

        self.assertListEqual([0], custom_list.data)
        self.assertEqual([0], result)

    def test_customListInsert_whenIndexIsNotInt_shouldRaise(self):
        index = "abc"
        value = 5

        custom_list = self.setup_list(1, 2, 3, 4)

        with self.assertRaises(CustomListTypeException) as context:
            custom_list.insert(index, value)

        self.assertIsNotNone(context.exception)
