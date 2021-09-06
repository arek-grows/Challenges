from __future__ import annotations
import unittest


def char_appears(string: str, search_for: str) -> list[int]:
    search_for = search_for.lower()
    string = string.lower().split()
    counts = []
    for ss in string:
        counts.append(ss.count(search_for))
    return counts  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            char_appears("She sells sea shells by the seashore.", "s"),
            [1, 2, 1, 2, 0, 0, 2],
        )

    def test_2(self):
        self.assertListEqual(
            char_appears("Peter Piper picked a peck of pickled peppers.", "p"),
            [1, 2, 1, 0, 1, 0, 1, 3],
        )

    def test_3(self):
        self.assertListEqual(
            char_appears("She hiked in the morning, then swam in the river.", "t"),
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        )

    def test_4(self):
        self.assertListEqual(
            char_appears("I scream, you scream, we all scream for ice cream.", "f"),
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        )

    def test_5(self):
        self.assertListEqual(char_appears("Snap, crackle, pop!", "p"), [1, 0, 2])

    def test_6(self):
        self.assertListEqual(char_appears("What a wonderful world.", "w"), [1, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()