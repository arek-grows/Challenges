from __future__ import annotations
import unittest


def will_hit(trajectory_slope: str, position: tuple[int, int]) -> bool:
    trajectory_slope = trajectory_slope.split()  # ['y', '=', 'mx', '+/-', 'b']
    x = trajectory_slope[2]
    x = int(x[:len(x) - 1])  # chop off 'x' at end of string and turn string into int
    b = int(trajectory_slope[4])
    if '-' in trajectory_slope:
        b *= -1
    if position[0] * x + b == position[1]:
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertFalse(will_hit("y = 2x - 5", (0, 0)))

    def test_2(self):
        self.assertTrue(will_hit("y = -4x + 6", (1, 2)))

    def test_3(self):
        self.assertFalse(will_hit("y = -4x + 6", (2, 2)))

    def test_4(self):
        self.assertTrue(will_hit("y = 3x - 8", (4, 4)))

    def test_5(self):
        self.assertFalse(will_hit("y = 2x + 6", (3, 2)))

    def test_6(self):
        self.assertTrue(will_hit("y = -3x + 15", (5, 0)))


if __name__ == "__main__":
    unittest.main()