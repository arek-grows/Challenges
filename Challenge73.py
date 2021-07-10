import unittest
import re


def alphanumeric_restriction(string: str) -> bool:
    if len(string) == 0:
        return False
    nums = '[0-9]'
    lets = '[a-zA-Z]'
    nums_match = re.findall(nums, string)
    lets_match = re.findall(lets, string)
    if len(nums_match) == len(string):
        return True
    elif len(lets_match) == len(string):
        return True
    return False  # Put your code here!!!


class TestAlphanumericRestriction(unittest.TestCase):
    def test_1(self):
        self.assertTrue(alphanumeric_restriction("Bold"))

    def test_2(self):
        self.assertTrue(alphanumeric_restriction("123454321"))

    def test_3(self):
        self.assertFalse(alphanumeric_restriction("H3LL0"))

    def test_4(self):
        self.assertTrue(alphanumeric_restriction("hhefuhiwfgn"))

    def test_5(self):
        self.assertTrue(alphanumeric_restriction("0"))

    def test_6(self):
        self.assertTrue(alphanumeric_restriction("hhefuhiwfgn"))

    def test_7(self):
        self.assertFalse(alphanumeric_restriction("ed@bit"))

    def test_8(self):
        self.assertFalse(alphanumeric_restriction("only letters right"))

    def test_9(self):
        self.assertFalse(alphanumeric_restriction("132 143 234"))

    def test_10(self):
        self.assertFalse(alphanumeric_restriction("()"))

    def test_11(self):
        self.assertTrue(alphanumeric_restriction("Hello"))

    def test_12(self):
        self.assertFalse(alphanumeric_restriction("10,000"))

    def test_13(self):
        self.assertFalse(alphanumeric_restriction("1a2b3c"))

    def test_14(self):
        self.assertFalse(alphanumeric_restriction(""))


if __name__ == "__main__":
    unittest.main()