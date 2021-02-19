from errors import CustomListSumException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListSumTests(CustomListTestBase):
    def test_customListSum_whenEmptyList_shouldReturn0(self):
        custom_list = self.setup_list()
        result = custom_list.sum()

        self.assertEqual(0, result)

    def test_customListSum_whenMultipleNumbers_shouldReturnTheirSum(self):
        custom_list = self.setup_list(1, 2)
        result = custom_list.sum()

        self.assertEqual(3, result)

    def test_customListSum_whenNumbersAndLenObjects_shouldReturnTheirSum(self):
        custom_list = self.setup_list(1, 2, '123')
        result = custom_list.sum()

        self.assertEqual(6, result)

    def test_customListSum_whenInvalidObjects_shouldRaise(self):
        custom_list = self.setup_list(1, 2, '123', object())

        with self.assertRaises(CustomListSumException) as context:
            custom_list.sum()

        self.assertIsNotNone(context.exception)
