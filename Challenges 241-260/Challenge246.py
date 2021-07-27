from __future__ import annotations
from typing import Any
import unittest


def convert_to_number(inventory: dict) -> dict:
    for i in inventory:
        inventory[i] = int(inventory[i])
    return inventory  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            convert_to_number({"piano": "200", "tv": "300", "stereo": "400"}),
            {"piano": 200, "tv": 300, "stereo": 400},
        )

    def test_2(self):
        self.assertEqual(
            convert_to_number({"piano": "200", "tv": "300"}), {"piano": 200, "tv": 300}
        )

    def test_3(self):
        self.assertEqual(convert_to_number({"piano": "200"}), {"piano": 200})

    def test_4(self):
        self.assertEqual(
            convert_to_number(
                {
                    "one": "1",
                    "two": "2",
                    "three": "3",
                    "four": "4",
                    "five": "5",
                    "six": "6",
                    "seven": "7",
                    "eight": "8",
                }
            ),
            {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
            },
        )


if __name__ == "__main__":
    unittest.main()