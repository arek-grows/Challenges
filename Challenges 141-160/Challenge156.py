from __future__ import annotations
from typing import Union
import unittest


def invert(dictionary: dict[str, Union[str, int]]) -> dict[Union[str, int], str]:
    new_dict = {}
    for d in dictionary:
        new_dict[dictionary[d]] = d
    return new_dict  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(invert({"a": 1, "b": 2, "c": 3}), {1: "a", 2: "b", 3: "c"})

    def test_2(self):
        self.assertEqual(invert({"z": "q", "w": "f"}), {"q": "z", "f": "w"})

    def test_3(self):
        self.assertEqual(invert({"zebra": "koala", "horse": "camel"}), {"koala": "zebra", "camel": "horse"})


if __name__ == "__main__":
    unittest.main()