from __future__ import annotations
import unittest


def guess_score(masterminds_code: str, guess: str) -> dict[str, int]:
    pegs = {"black": 0, "white": 0}
    masterminds_code = list(masterminds_code)
    for x, num in enumerate(guess):
        if (num in masterminds_code) and (masterminds_code[x] == num):
            pegs["black"] += 1
            masterminds_code[x] = 'a'
    return {}  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(guess_score("1423", "5678"), {"black": 0, "white": 0})

    def test_2(self):
        self.assertEqual(guess_score("1423", "2222"), {"black": 1, "white": 0})

    def test_3(self):
        self.assertEqual(guess_score("1423", "1234"), {"black": 1, "white": 3})

    def test_4(self):
        self.assertEqual(guess_score("1423", "2211"), {"black": 0, "white": 2})

    def test_5(self):
        self.assertEqual(guess_score("2928", "7722"), {"black": 1, "white": 1})

    def test_6(self):
        self.assertEqual(guess_score("4845", "6446"), {"black": 1, "white": 1})


if __name__ == "__main__":
    unittest.main()