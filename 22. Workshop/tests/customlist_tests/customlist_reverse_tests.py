from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListReverseTests(CustomListTestBase):
    def test_customListReverse_whenEmptyList_shouldReturnEmpty(self):
        custom_list = self.setup_list()
        result = custom_list.reverse()

        self.assertEmpty(result)

    def test_customListReverse_whenListIsNotEmpty_shouldReturnReversed(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.reverse()

        self.assertListEqual([4, 3, 2, 1], result)

    def test_customListReverse_whenSingleElement_shouldReturnIt(self):
        custom_list = self.setup_list(1)
        result = custom_list.reverse()

        self.assertListEqual([1], result)
