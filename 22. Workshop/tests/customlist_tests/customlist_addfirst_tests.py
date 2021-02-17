from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListAddFirstTests(CustomListTestBase):
    def test_customListAddFirst_whenNonEmptyList_shouldAddElementAtTheBeginning(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        custom_list.add_first(5)

        self.assertListEqual([5, 1, 2, 3, 4], custom_list.data)

    def test_customListAddFirst_whenListIsEmpty_shouldAddElement(self):
        custom_list = self.setup_list()
        custom_list.add_first(5)

        self.assertListEqual([5], custom_list.data)
