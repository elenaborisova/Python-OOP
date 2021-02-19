from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListDictionarizeTests(CustomListTestBase):
    def test_customListDictionarize_whenEmptyList_shouldReturnEmptyDict(self):
        custom_list = self.setup_list()
        result = custom_list.dictionize()

        self.assertEmpty(result)

    def test_customListDictionarize_whenEvenCountElements_shouldReturnDict(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.dictionize()

        self.assertDictEqual({1: 2, 3: 4}, result)

    def test_customListDictionarize_whenOddCountElements_shouldReturnDictWithSpace(self):
        custom_list = self.setup_list(1, 2, 3, 4, 5)
        result = custom_list.dictionize()

        self.assertDictEqual({1: 2, 3: 4, 5: ' '}, result)
