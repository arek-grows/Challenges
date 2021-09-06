from __future__ import annotations
import unittest


def even_odd_transform(numbers: list[int], iterations: int) -> list[int]:
    end = []
    for nn in numbers:
        if nn % 2 == 0:
            end.append(nn + -2 * iterations)
        else:
            end.append(nn + 2 * iterations)
    return end  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(even_odd_transform([3, 4, 9], 3), [9, -2, 15])

    def test_2(self):
        self.assertListEqual(even_odd_transform([0, 0, 0], 10), [-20, -20, -20])

    def test_3(self):
        self.assertListEqual(even_odd_transform([1, 2, 3], 1), [3, 0, 5])

    def test_4(self):
        self.assertListEqual(even_odd_transform([55, 90, 830], 2), [59, 86, 826])


if __name__ == "__main__":
    unittest.main()