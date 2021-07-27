import unittest


def multiply_nums(nums: str) -> int:
    nums = nums.split(", ")
    total = 1
    for n in nums:
        total *= int(n)
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, multiply_nums("2, 3"))

    def test_2(self):
        self.assertEqual(24, multiply_nums("1, 2, 3, 4"))

    def test_3(self):
        self.assertEqual(0, multiply_nums("54, 75, 453, 0"))

    def test_4(self):
        self.assertEqual(-20, multiply_nums("10, -2"))

    def test_5(self):
        self.assertEqual(160056, multiply_nums("-26, 1, -27, -12, -19"))

    def test_6(self):
        self.assertEqual(128, multiply_nums("16, 8"))

    def test_7(self):
        self.assertEqual(2339064, multiply_nums("-27, -14, -28, 13, -17"))

    def test_8(self):
        self.assertEqual(-4082823360000, multiply_nums("-19, -22, -14, 20, -15, -24, -17, 19, 30, -10"))

    def test_9(self):
        self.assertEqual(0, multiply_nums("1, 13, 0, -11, 26, -17, 21"))

    def test_10(self):
        self.assertEqual(2247700, multiply_nums("-25, -19, 7, -26, -26"))


if __name__ == "__main__":
    unittest.main()