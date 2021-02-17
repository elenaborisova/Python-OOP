from errors import CustomListIndexException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListPopTests(CustomListTestBase):
    def test_customListPop_whenNonEmptyList_shouldRemoveAndReturnLastElement(self):
        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.pop()

        self.assertListEqual([1, 2, 3], custom_list.data)
        self.assertEqual(4, result)

    def test_customListPop_whenListIsEmpty_shouldRaise(self):
        custom_list = self.setup_list()

        with self.assertRaises(CustomListIndexException) as context:
            custom_list.pop()

        self.assertIsNotNone(context.exception)
