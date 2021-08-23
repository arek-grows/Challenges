from typing import Callable
import unittest


def which_is_larger(f: Callable[[], int], g: Callable[[], int]) -> str:
    f = f()
    g = g()
    if f == g:
        return "neither"
    if f > g:
        return "f"
    return "g"  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(which_is_larger(lambda: 5, lambda: 10), "g")

    def test_2(self):
        self.assertEqual(which_is_larger(lambda: 10, lambda: 5), "f")

    def test_3(self):
        self.assertEqual(which_is_larger(lambda: 25, lambda: 25), "neither")

    def test_4(self):
        self.assertEqual(which_is_larger(lambda: -100, lambda: -100), "neither")

    def test_5(self):
        self.assertEqual(which_is_larger(lambda: -100, lambda: 0), "g")

    def test_6(self):
        self.assertEqual(which_is_larger(lambda: 505050, lambda: 5050), "f")

    def test_7(self):
        self.assertEqual(which_is_larger(lambda: 100, lambda: 1000), "g")


if __name__ == "__main__":
    unittest.main()