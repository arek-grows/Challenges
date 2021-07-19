import unittest


def is_curzon(num: int) -> bool:
    if (2 ** num + 1) % (2 * num + 1) == 0:
        return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_curzon(5))

    def test_2(self):
        self.assertFalse(is_curzon(10))

    def test_3(self):
        self.assertTrue(is_curzon(14))

    def test_4(self):
        self.assertTrue(is_curzon(86))

    def test_5(self):
        self.assertTrue(is_curzon(90))

    def test_6(self):
        self.assertFalse(is_curzon(115))

    def test_7(self):
        self.assertFalse(is_curzon(120))

    def test_8(self):
        self.assertTrue(is_curzon(194))

    def test_9(self):
        self.assertTrue(is_curzon(293))


if __name__ == "__main__":
    unittest.main()