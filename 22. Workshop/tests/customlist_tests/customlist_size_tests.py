from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListSizeTests(CustomListTestBase):
    def test_customListSize_whenEmptyList_shouldReturn0(self):
        custom_list = self.setup_list()
        result = custom_list.size()

        self.assertEqual(0, result)

    def test_customListSize_whenNonEmptyList_shouldReturnLenOfList(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.size()

        self.assertEqual(4, result)

