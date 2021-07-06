import unittest
import re


def transform(word: str) -> str:

    return ""  # Put your code here!!!


class TestTransform(unittest.TestCase):
    def test_1(self):
        self.assertEqual("01110", transform("house"))

    def test_2(self):
        self.assertEqual("0100000", transform("excLAIM"))

    def test_3(self):
        self.assertEqual("0111", transform("moon"))

    def test_4(self):
        self.assertEqual("0111", transform("MOOn"))

    def test_5(self):
        self.assertEqual("1111111111", transform("topsyTurvy"))


if __name__ == "__main__":
    unittest.main()