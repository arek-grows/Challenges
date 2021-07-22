import unittest


def round_number(num: int, n: int) -> int:
    closest = 0
    for x in range(num - n, num + n + 1):
        if x % n == 0:
            # if the next divisible number is higher than num and the difference between the last divisible number is
            # bigger
            if closest != 0 and abs(closest - num) < abs(x - num):
                return closest
            # if there are two divisible numbers of equal distance to n, return the higher one
            elif closest != 0 and abs(closest - num) == abs(x - num):
                return x
            else:
                closest = x
    return closest  # Put your code here!!!


class TestRoundNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(round_number(34, 25), 25)

    def test_2(self):
        self.assertEqual(round_number(54, 8), 56)

    def test_3(self):
        self.assertEqual(round_number(65, 10), 70)

    def test_4(self):
        self.assertEqual(round_number(6247, 163), 6194)

    def test_5(self):
        self.assertEqual(round_number(532, 12), 528)

    def test_6(self):
        self.assertEqual(round_number(642234, 1523), 642706)

    def test_7(self):
        self.assertEqual(round_number(5123, 10), 5120)

    def test_8(self):
        self.assertEqual(round_number(96623443, 7650), 96627150)

    def test_9(self):
        self.assertEqual(round_number(125123, 520), 125320)

    def test_10(self):
        self.assertEqual(round_number(12121212, 144), 12121200)



if __name__ == "__main__":
    unittest.main()