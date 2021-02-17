from unittest import TestCase


class TestCaseBase(TestCase):
    def assertEmpty(self, iterable):
        return self.assertEqual([], list(iterable))
