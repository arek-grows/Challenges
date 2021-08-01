import unittest


def fit(crate_x: int, crate_y: int, package_w: int, package_l: int) -> int:
    return (crate_x // package_w) * (crate_y // package_l)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(12, fit(25, 18, 6, 5))

    def test_2(self):
        self.assertEqual(100, fit(10, 10, 1, 1))

    def test_3(self):
        self.assertEqual(10, fit(12, 34, 5, 6))

    def test_4(self):
        self.assertEqual(5676, fit(12345, 678910, 1112, 1314))

    def test_5(self):
        self.assertEqual(0, fit(5, 100, 6, 1))


if __name__ == "__main__":
    unittest.main()