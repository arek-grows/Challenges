# Challenge 191 - Next Number Greater Than A and B and Divisible by B
#
# You are given two numbers a and b. Create a function that returns the next number greater than a and b that is divisible by b.
# Examples
#
# divisible_by_b(17, 8) ➞ 24
#
# divisible_by_b(98, 3) ➞ 99
#
# divisible_by_b(14, 11) ➞ 22


import unittest


def divisible_by_b(a: int, b: int) -> int:
    while True:
        a += 1
        if a % b == 0:
            return a


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(divisible_by_b(17, 8), 24)

    def test_2(self):
        self.assertEqual(divisible_by_b(98, 3), 99)

    def test_3(self):
        self.assertEqual(divisible_by_b(14, 11), 22)

    def test_4(self):
        self.assertEqual(divisible_by_b(11, 8), 16)

    def test_5(self):
        self.assertEqual(divisible_by_b(450, 36), 468)

    def test_6(self):
        self.assertEqual(divisible_by_b(1019, 13), 1027)


if __name__ == "__main__":
    unittest.main()