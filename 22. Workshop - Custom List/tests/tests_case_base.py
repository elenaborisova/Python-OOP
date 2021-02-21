from unittest import TestCase


class TestCaseBase(TestCase):
    def assertEmpty(self, iterable):
        if type(iterable) == dict:
            return self.assertDictEqual({}, dict(iterable))
        elif type(iterable) == set:
            return self.assertSetEqual(set(), set(iterable))

        return self.assertListEqual([], list(iterable))
