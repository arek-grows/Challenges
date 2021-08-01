import unittest


def tax(income: int) -> int:

    return round(total_tax)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, tax(0))

    def test_2(self):
        self.assertEqual(0, tax(10_000))

    def test_3(self):
        self.assertEqual(0, tax(10_009))

    def test_4(self):
        self.assertEqual(1, tax(10_010))

    def test_5(self):
        self.assertEqual(200, tax(12_000))

    def test_6(self):
        self.assertEqual(8_697, tax(56_789))

    def test_7(self):
        self.assertEqual(473_326, tax(1_234_567))


if __name__ == "__main__":
    unittest.main()