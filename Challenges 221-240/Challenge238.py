from __future__ import annotations
import unittest


def count_uppercase(words: list[str]) -> int:
    total = 0
    for word in words:
        for c in word:
            if c.isupper():
                total += 1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_uppercase(["SOLO", "hello", "Tea", "wHat"]), 6)

    def test_2(self):
        self.assertEqual(count_uppercase(["little", "lower", "down"]), 0)

    def test_3(self):
        self.assertEqual(count_uppercase(["BEGinner", "Dot", "Py"]), 5)


if __name__ == "__main__":
    unittest.main()