from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListCountTests(CustomListTestBase):
    def test_customListCount_whenListContainsValueMultipleTimes_shouldReturnItsCount(self):
        value = 4

        custom_list = self.setup_list(1, 2, 3, 4, 4, 4)
        result = custom_list.count(value)

        self.assertEqual(3, result)

    def test_customListCount_whenListContainsValueSingleTime_shouldReturn1(self):
        value = 4

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.count(value)

        self.assertEqual(1, result)

    def test_customListCount_whenValueNotInList_shouldReturn0(self):
        value = 5

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.count(value)

        self.assertEqual(0, result)

    def test_customListCount_whenListIsEmpty_shouldReturn0(self):
        value = 5

        custom_list = self.setup_list()
        result = custom_list.count(value)

        self.assertEqual(0, result)
