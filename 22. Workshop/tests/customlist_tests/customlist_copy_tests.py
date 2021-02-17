from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListCopyTests(CustomListTestBase):
    def test_customListCopy_whenEmptyList_shouldReturnCustomEmptyList(self):
        custom_list = self.setup_list()
        result = custom_list.copy()

        self.assertNotEqual(custom_list, result)
        self.assertListEqual(custom_list.data, result.data)

    def test_customListCopy_whenNonEmptyList_shouldReturnCustomEmptyList(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.copy()

        self.assertNotEqual(custom_list, result)
        self.assertListEqual(custom_list.data, result.data)
