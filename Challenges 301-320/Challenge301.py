from __future__ import annotations
from typing import Any
import unittest


def match_last_item(items: list[Any]) -> bool:
    end = ""
    for i in items[:len(items) - 1]:
        end += str(i)
    return end == items[-1]  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))

    def test_2(self):
        self.assertFalse(match_last_item([0, 1, 2, 3, 4, 5, "12345"]))

    def test_3(self):
        self.assertFalse(match_last_item(["for", "mi", "da", "bel", "formidable"]))

    def test_4(self):
        self.assertTrue(match_last_item([8, "thunder", True, "8thunderTrue"]))

    def test_5(self):
        self.assertFalse(match_last_item([1, 1, 1, "11"]))


if __name__ == "__main__":
    unittest.main()