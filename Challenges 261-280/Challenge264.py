from __future__ import annotations
import unittest


def count_all(string: str) -> dict[str, int]:
    alphanumerics = {"LETTERS": 0, "DIGITS": 0}
    for s in string:
        if s.isalpha():
            alphanumerics["LETTERS"] += 1
        elif s.isdigit():
            alphanumerics["DIGITS"] += 1
    return alphanumerics  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_all("Hello"), {"LETTERS": 5, "DIGITS": 0})

    def test_2(self):
        self.assertEqual(count_all("137"), {"LETTERS": 0, "DIGITS": 3})

    def test_3(self):
        self.assertEqual(count_all("H3LL0"), {"LETTERS": 3, "DIGITS": 2})

    def test_4(self):
        self.assertEqual(count_all("149990"), {"LETTERS": 0, "DIGITS": 6})

    def test_5(self):
        self.assertEqual(
            count_all("Beginner.py 2021"),
            {"LETTERS": 10, "DIGITS": 4},
        )

    def test_6(self):
        self.assertEqual(count_all("    "), {"LETTERS": 0, "DIGITS": 0})


if __name__ == "__main__":
    unittest.main()
