import unittest


def unusual_subtraction(n: int, k: int) -> int:
    for x in range(k):
        if str(n)[-1] == '0':
            n = int(str(n)[:-1])
        else:
            n -= 1
    return n  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(unusual_subtraction(78, 9), 7)

    def test_2(self):
        self.assertEqual(unusual_subtraction(540, 5), 50)

    def test_3(self):
        self.assertEqual(unusual_subtraction(1000000000, 9), 1)

    def test_4(self):
        self.assertEqual(unusual_subtraction(420, 4), 4)

    def test_5(self):
        self.assertEqual(unusual_subtraction(42023110, 10), 4201)

    def test_6(self):
        self.assertEqual(unusual_subtraction(88888888, 50), 883)


if __name__ == "__main__":
    unittest.main()