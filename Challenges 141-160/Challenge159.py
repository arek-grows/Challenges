from __future__ import annotations
import unittest


def face_interval(numbers: list[int]) -> str:
    if (max(numbers) - min(numbers)) in numbers:
        return ":)"
    return ":("  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(face_interval([1, 2, 5, 8, 3, 9]), ":)")

    def test_2(self):
        self.assertEqual(face_interval([5, 2, 6, 3, 11]), ":(")

    def test_3(self):
        self.assertEqual(face_interval([20, 50, 13, 60, 79, 72, 99]), ":(")

    def test_4(self):
        self.assertEqual(face_interval([11, 42, 83, 28, 47, 94]), ":)")


if __name__ == "__main__":
    unittest.main()