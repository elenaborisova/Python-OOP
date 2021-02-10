from unittest import TestCase
from custom_list import CustomList


class CustomListTestBase(TestCase):
    def setup_list(self, *args):
        custom_list = CustomList()
        [custom_list.append(x) for x in args]
        return custom_list
