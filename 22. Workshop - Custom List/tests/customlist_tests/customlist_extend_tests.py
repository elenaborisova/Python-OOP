from errors import CustomListTypeException
from tests.customlist_tests.base.customlist_test_base import CustomListTestBase


class CustomListExtendTests(CustomListTestBase):
    def test_customListExtend_whenNonEmptyAndExtendedNonEmpty_shouldExtendAndReturnList(self):
        value = [5, 6, 7]

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.extend(value)

        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], custom_list.data)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], result)

    def test_customListExtend_whenEmptyAndExtendedNonEmpty_shouldExtendAndReturnList(self):
        value = [5, 6, 7]

        custom_list = self.setup_list()
        result = custom_list.extend(value)

        self.assertListEqual([5, 6, 7], custom_list.data)
        self.assertListEqual([5, 6, 7], result)

    def test_customListExtend_whenNonEmptyAndExtendedEmpty_shouldExtendAndReturnList(self):
        value = []

        custom_list = self.setup_list(1, 2, 3, 4)
        result = custom_list.extend(value)

        self.assertListEqual([1, 2, 3, 4], custom_list.data)
        self.assertListEqual([1, 2, 3, 4], result)

    def test_customListExtend_whenEmptyAndCustomIterable_shouldExtendAndReturnList(self):
        class CustomIterable:
            def __init__(self, value):
                self.is_done = False
                self.value = value

            def __iter__(self):
                return self

            def __next__(self):
                if self.is_done:
                    raise StopIteration()
                self.is_done = True
                return self.value

        value = CustomIterable(1)

        custom_list = self.setup_list()
        result = custom_list.extend(value)

        self.assertListEqual([1], custom_list.data)
        self.assertListEqual([1], result)

    def test_customListExtend_whenExtendedNotIterable_shouldRaise(self):
        value = 5

        custom_list = self.setup_list(1, 2, 3, 4)

        with self.assertRaises(CustomListTypeException) as context:
            custom_list.extend(value)

        self.assertIsNotNone(context.exception)

