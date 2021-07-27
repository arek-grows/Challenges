from __future__ import annotations
import unittest


def time(rate: dict[str, int], minutes: int, walls: int) -> int:
    paint_rate = rate['walls'] / rate['people']
    paint_rate = paint_rate / rate['minutes']
    return walls/minutes/paint_rate  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        rate1 = {"people": 4, "walls": 9, "minutes": 63}
        self.assertEqual(time(rate1, 7, 4), 16)

    def test_2(self):
        rate2 = {"people": 10, "walls": 10, "minutes": 22}
        self.assertEqual(time(rate2, 10, 10), 22)

    # Original JavaScript challenge by Isaac Pak.


if __name__ == "__main__":
    unittest.main()