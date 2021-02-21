from custom_list import CustomList
from tests.tests_case_base import TestCaseBase


class CustomListTestBase(TestCaseBase):
    def setup_list(self, *args):
        custom_list = CustomList()
        [custom_list.append(x) for x in args]
        return custom_list
