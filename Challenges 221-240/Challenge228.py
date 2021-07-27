# Challenge 228 - Add Suffix
#
# Write a function that returns a lambda expression, which transforms its input by adding a particular suffix at the end.
# Examples
#
# add_ly = add_suffix("ly")
#
# add_ly("hopeless") ➞ "hopelessly"
# add_ly("total") ➞ "totally"
#
# add_less = add_suffix("less")
#
# add_less("fear") ➞ "fearless"
# add_less("ruth") ➞ "ruthless"


from typing import Callable
import unittest


def add_suffix(suffix: str) -> Callable[[str], str]:
    return lambda x: x + suffix  # Put your code here!!!


class Tests(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.add_ing = add_suffix("ing")
        self.add_less = add_suffix("less")
        self.add_ly = add_suffix("ly")

    def test_1(self):
        self.assertEqual(self.add_ly("hopeless"), "hopelessly")

    def test_2(self):
        self.assertEqual(self.add_ly("total"), "totally")

    def test_3(self):
        self.assertEqual(self.add_less("fear"), "fearless")

    def test_4(self):
        self.assertEqual(self.add_less("ruth"), "ruthless")

    def test_5(self):
        self.assertEqual(self.add_ing("cheer"), "cheering")

    def test_6(self):
        self.assertEqual(self.add_ing("book"), "booking")


if __name__ == "__main__":
    unittest.main()