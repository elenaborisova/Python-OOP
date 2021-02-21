from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListAppendTests(CustomListTestBase):
    def test_customListAppend_whenEmptyList_shouldReturnListWithTheElement(self):
        value = 5

        custom_list = self.setup_list()
        result = custom_list.append(value)

        self.assertListEqual([value], result)

    def test_customListAppend_whenListIsNotEmpty_shouldReturnListWithNewElementAtTheEnd(self):
        value = 3

        custom_list = self.setup_list(1, 2)
        result = custom_list.append(value)

        self.assertListEqual([1, 2, value], result)
