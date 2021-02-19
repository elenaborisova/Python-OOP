from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListOverboundTests(CustomListTestBase):
    def test_customListOverbound_whenMultipleNumbers_shouldReturnTheIndexOfTheMaxElement(self):
        custom_list = self.setup_list(1, 2, 3)
        result = custom_list.overbound()

        self.assertEqual(2, result)

    def test_customListOverbound_whenNumbersAndLenObjects_shouldReturnTheIndexOfTheMaxElement(self):
        custom_list = self.setup_list(1, 2, '123')
        result = custom_list.overbound()

        self.assertEqual(2, result)
