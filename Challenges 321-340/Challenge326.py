from __future__ import annotations
import unittest


def find_a_seat(max_capacity: int, car_occupancies: list[int]) -> int:
    half_capacity = max_capacity / len(car_occupancies) / 2
    for idx, cc in enumerate(car_occupancies):
        if cc <= half_capacity:
            return idx
    return -1  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_a_seat(20, [3, 5, 4, 2]), 3)

    def test_2(self):
        self.assertEqual(find_a_seat(1000, [50, 20, 80, 90, 100, 60, 30, 50, 80, 60]), 0)

    def test_3(self):
        self.assertEqual(find_a_seat(200, [35, 23, 40, 21, 38]), -1)

    def test_4(self):
        self.assertEqual(find_a_seat(200, [35, 23, 18, 10, 40]), 2)

    def test_5(self):
        self.assertEqual(find_a_seat(21, [6, 3, 7]), 1)

    def test_6(self):
        self.assertEqual(find_a_seat(11037, [1839, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()