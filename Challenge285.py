from __future__ import annotations
import unittest


def letter_counter(word_search: list[list[str]], letter: str) -> int:
    total = 0
    for row in word_search:
        total += row.count(letter)
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            letter_counter([
                ["D", "E", "Y", "H", "A", "D"],
                ["C", "B", "Z", "Y", "J", "K"],
                ["D", "B", "C", "A", "M", "N"],
                ["F", "G", "G", "R", "S", "R"],
                ["V", "X", "H", "A", "S", "S"],
            ], "D"),
            3,
        )

    def test_2(self):
        self.assertEqual(
            letter_counter([
                ["D", "E", "Y", "H", "A", "D"],
                ["C", "B", "Z", "Y", "J", "K"],
                ["D", "B", "C", "A", "M", "N"],
                ["F", "G", "G", "R", "S", "R"],
                ["V", "X", "H", "A", "S", "S"],
            ], "H"),
            2,
        )

    def test_3(self):
        self.assertEqual(
            letter_counter([
                ["D", "E", "Y", "H", "A", "D"],
                ["C", "B", "Z", "Y", "J", "K"],
                ["D", "B", "C", "A", "M", "N"],
                ["F", "G", "G", "R", "S", "R"],
                ["V", "X", "H", "A", "S", "S"],
            ], "Z"),
            1,
        )


if __name__ == "__main__":
    unittest.main()