from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListUnderboundTests(CustomListTestBase):
    def test_customListUnderbound_whenMultipleNumbers_shouldReturnTheIndexOfTheMinElement(self):
        custom_list = self.setup_list(1, 2, 3)
        result = custom_list.underbound()

        self.assertEqual(0, result)

    def test_customListUnderbound_whenNumbersAndLenObjects_shouldReturnTheIndexOfTheMinElement(self):
        custom_list = self.setup_list('1', 2, 3)
        result = custom_list.underbound()

        self.assertEqual(0, result)
