from __future__ import annotations
from typing import Union
import unittest


def to_list(dct: dict[str, int]) -> list[list[Union[str, int]]]:
    end = [[a, b] for a, b in dct.items()]
    end.sort()
    return end  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(to_list({"a": 1, "b": 2}), [["a", 1], ["b", 2]])

    def test_2(self):
        self.assertListEqual(
            to_list({"foo": 33, "bar": 45, "baz": 67}),
            [["bar", 45], ["baz", 67], ["foo", 33]],
        )

    def test_3(self):
        self.assertListEqual(
            to_list({"shrimp": 15, "tots": 12}), [["shrimp", 15], ["tots", 12]]
        )

    def test_4(self):
        self.assertListEqual(to_list({}), [])


if __name__ == "__main__":
    unittest.main()