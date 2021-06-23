import unittest


def total_overs(balls: int) -> float:
    total = balls//6
    total += (balls % 6) * 0.1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(total_overs(2400), 400)

    def test_2(self):
        self.assertEqual(total_overs(164), 27.2)

    def test_3(self):
        self.assertEqual(total_overs(945), 157.3)

    def test_4(self):
        self.assertEqual(total_overs(5), 0.5)

    def test_5(self):
        self.assertEqual(total_overs(7), 1.1)

    def test_6(self):
        self.assertEqual(total_overs(15), 2.3)

    def test_7(self):
        self.assertEqual(total_overs(0), 0)


if __name__ == "__main__":
    unittest.main()