import unittest


def is_automorphic(number: int) -> bool:
    squared = str(number ** 2)
    number = str(number)
    return number == squared[len(squared) - len(number):]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_automorphic(0))

    def test_2(self):
        self.assertTrue(is_automorphic(1))

    def test_3(self):
        self.assertTrue(is_automorphic(5))

    def test_4(self):
        self.assertTrue(is_automorphic(6))

    def test_5(self):
        self.assertTrue(is_automorphic(25))

    def test_6(self):
        self.assertTrue(is_automorphic(76))

    def test_7(self):
        self.assertTrue(is_automorphic(7109376))

    def test_8(self):
        self.assertTrue(is_automorphic(18212890625))

    def test_9(self):
        self.assertFalse(is_automorphic(36))

    def test_10(self):
        self.assertFalse(is_automorphic(100))

    def test_11(self):
        self.assertFalse(is_automorphic(11))

    def test_12(self):
        self.assertFalse(is_automorphic(6025))

    def test_13(self):
        self.assertFalse(is_automorphic(3))

    def test_14(self):
        self.assertFalse(is_automorphic(81787108376))

    def test_15(self):
        self.assertFalse(is_automorphic(1376))


if __name__ == "__main__":
    unittest.main()