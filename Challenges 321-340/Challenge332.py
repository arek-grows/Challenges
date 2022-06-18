from __future__ import annotations
import unittest


def num_split(number: int) -> list[int]:
    number_string = str(number)
    multiplier = 1
    if number < 0:
        multiplier = -1
        number_string = number_string[1:]
    number_string = number_string[::-1]
    split_numbers = []

    for nn in number_string:
        split_numbers.append(int(nn) * multiplier)
        multiplier *= 10

    return split_numbers[::-1]  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(num_split(39), [30, 9])

    def test_2(self):
        self.assertListEqual(num_split(-434), [-400, -30, -4])

    def test_3(self):
        self.assertListEqual(num_split(100), [100, 0, 0])

    def test_4(self):
        self.assertListEqual(num_split(3929), [3000, 900, 20, 9])

    def test_5(self):
        self.assertListEqual(num_split(10293), [10000, 0, 200, 90, 3])

    def test_6(self):
        self.assertListEqual(num_split(900), [900, 0, 0])

    def test_7(self):
        self.assertListEqual(num_split(-100), [-100, 0, 0])


if __name__ == "__main__":
    unittest.main()