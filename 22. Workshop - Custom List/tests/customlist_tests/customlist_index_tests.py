from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListIndexTests(CustomListTestBase):
    def test_customListIndex_whenValueInList_shouldReturnIndexOfValue(self):
        value = 4

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.index(value)

        self.assertEqual(3, result)

    def test_customListIndex_whenListContainsValueMultipleTimes_shouldReturnTheLeftmostIndex(self):
        value = 4

        custom_list = self.setup_list(1, 2, 3, 4, 4)
        result = custom_list.index(value)

        self.assertEqual(3, result)

    def test_customListIndex_whenValueNotInList_shouldReturnMinusOne(self):
        value = 5

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.index(value)

        self.assertEqual(-1, result)

    def test_customListIndex_whenListIsEmpty_shouldReturnMinusOne(self):
        value = 5

        custom_list = self.setup_list()
        result = custom_list.index(value)

        self.assertEqual(-1, result)




