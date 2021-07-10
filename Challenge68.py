import unittest


def halve_count(a: int, b: int) -> int:
    total = 0
    while a > b:
        a /= 2
        if b > a:
            return total
        total += 1
    return total


class TestHalveCount(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, halve_count(1891, 4))

    def test_2(self):
        self.assertEqual(6, halve_count(1756, 14))

    def test_3(self):
        self.assertEqual(11, halve_count(7764, 2))

    def test_4(self):
        self.assertEqual(4, halve_count(1118, 47))

    def test_5(self):
        self.assertEqual(1, halve_count(161, 79))

    def test_6(self):
        self.assertEqual(7, halve_count(8573, 35))

    def test_7(self):
        self.assertEqual(12, halve_count(4123, 1))

    def test_8(self):
        self.assertEqual(4, halve_count(1348, 60))

    def test_9(self):
        self.assertEqual(7, halve_count(7549, 31))

    def test_10(self):
        self.assertEqual(9, halve_count(4469, 5))


if __name__ == "__main__":
    unittest.main()