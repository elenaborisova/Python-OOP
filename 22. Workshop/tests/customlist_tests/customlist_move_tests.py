from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListMoveFirstTests(CustomListTestBase):
    def test_customListMove_whenListIsEmpty_shouldReturnEmptyList(self):
        custom_list = self.setup_list()
        result = custom_list.move(5)

        self.assertEmpty(result)

    def test_customListMove_whenSingleElement_shouldReturnIt(self):
        custom_list = self.setup_list(1)
        result = custom_list.move(5)

        self.assertListEqual([1], result)
        self.assertListEqual([1], custom_list.data)

    def test_customListMove_whenMultipleElements_shouldMoveThemAndReturnList(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.move(2)

        self.assertListEqual([3, 4, 1, 2], result)
        self.assertListEqual([3, 4, 1, 2], custom_list.data)

    # def move(self, amount):
    #     self.__data = self.__data[amount:] + self.__data[:amount]
    #     return self.__data
