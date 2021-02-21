from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListClearTests(CustomListTestBase):
    def test_customListClear_whenNonEmptyList_shouldClear(self):
        custom_list = self.setup_list(1, 2, 3, 4)

        custom_list.clear()

        self.assertEmpty(custom_list)

    def test_customListClear_whenListIsEmpty_shouldClear(self):
        custom_list = self.setup_list()

        custom_list.clear()

        self.assertEmpty(custom_list)


