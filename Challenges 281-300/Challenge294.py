from __future__ import annotations
from typing import Union
import unittest


def multiply(lst: list[Union[int, str]]) -> list[list[Union[int, str]]]:
    length = len(lst)
    end_list = []
    for x in range(0, length):
        end_list.append([lst[x]] * length)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            multiply(["*", "%", "$"]),
            [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]],
        )

    def test_2(self):
        self.assertListEqual(multiply([4, 5]), [[4, 4], [5, 5]])

    def test_3(self):
        self.assertListEqual(
            multiply(["A", "B", "C", "D", "E"]),
            [
                ["A", "A", "A", "A", "A"],
                ["B", "B", "B", "B", "B"],
                ["C", "C", "C", "C", "C"],
                ["D", "D", "D", "D", "D"],
                ["E", "E", "E", "E", "E"],
            ],
        )

    def test_4(self):
        self.assertListEqual(multiply([1]), [[1]])


if __name__ == "__main__":
    unittest.main()