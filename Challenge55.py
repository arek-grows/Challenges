import unittest


def add_x_times(a, b):
    if b == 0:
        return a
    return add_x_times(a * 2, b - 1)


def abcmath(a: int, b: int, c: int) -> int:
    if add_x_times(a, b) % c == 0:
        return True
    return False  # Put your code here!


class TestMultiDivision(unittest.TestCase):
    def test_1(self):
        self.assertFalse(abcmath(1, 2, 3))

    def test_2(self):
        self.assertFalse(abcmath(69, 15, 9))

    def test_3(self):
        self.assertFalse(abcmath(9, 2, 52))

    def test_4(self):
        self.assertFalse(abcmath(5, 2, 3))

    def test_5(self):
        self.assertTrue(abcmath(5, 2, 1))

    def test_6(self):
        self.assertTrue(abcmath(261, 2, 1))

    def test_7(self):
        self.assertTrue(abcmath(22, 2, 22))

    def test_8(self):
        self.assertTrue(abcmath(69, 12, 3))


if __name__ == "__main__":
    unittest.main()