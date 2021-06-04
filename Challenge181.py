import unittest

import math


def is_sastry(number: int) -> bool:
    concat = int(str(number) + str(number + 1))
    square_root_int = int(math.sqrt(concat))
    return square_root_int*square_root_int == concat  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_sastry(183))

    def test_2(self):
        self.assertFalse(is_sastry(184))

    def test_3(self):
        self.assertTrue(is_sastry(106755))

    def test_4(self):
        self.assertFalse(is_sastry(129987253440921))

    def test_5(self):
        self.assertTrue(is_sastry(157175907513603))

    def test_6(self):
        self.assertTrue(is_sastry(206611570247935))

    def test_7(self):
        self.assertFalse(is_sastry(338752188230098))

    def test_8(self):
        self.assertTrue(is_sastry(433610247875715))

    def test_9(self):
        self.assertFalse(is_sastry(652333983478884))

    def test_10(self):
        self.assertTrue(is_sastry(718717107443715))

    def test_11(self):
        self.assertFalse(is_sastry(752199872453889))

    def test_12(self):
        self.assertTrue(is_sastry(786704531939448))


if __name__ == "__main__":
    unittest.main()