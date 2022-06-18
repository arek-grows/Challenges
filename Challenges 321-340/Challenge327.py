import unittest
from math import sqrt


def check_perfect(n: int) -> bool:
    factor_list = []
    square_root = sqrt(n)

    if square_root.is_integer():
        square_root = int(square_root)
        factor_list.append(square_root)
    else:
        square_root = int(square_root) + 1

    for xx in range(1, square_root):
        quotient = n / xx
        if quotient.is_integer():
            factor_list.append(int(quotient))
            factor_list.append(xx)

    factor_list.sort()
    factor_list.remove(n)

    return sum(factor_list) == n


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_perfect(6))

    def test_2(self):
        self.assertTrue(check_perfect(28))

    def test_3(self):
        self.assertTrue(check_perfect(496))

    def test_4(self):
        self.assertTrue(check_perfect(8128))

    def test_5(self):
        self.assertTrue(check_perfect(33550336))

    def test_6(self):
        self.assertFalse(check_perfect(12))

    def test_7(self):
        self.assertFalse(check_perfect(97))

    def test_8(self):
        self.assertFalse(check_perfect(481))

    def test_9(self):
        self.assertFalse(check_perfect(1001))

    def test_10(self):
        self.assertFalse(check_perfect(55555))


if __name__ == "__main__":
    unittest.main()