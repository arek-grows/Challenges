import unittest


def digit_distance(num_a: int, num_b: int) -> int:
    num_a = str(num_a)
    num_b = str(num_b)
    distance = 0
    for aa, bb in zip(num_a, num_b):
        distance += abs(int(aa) - int(bb))
    return distance  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(digit_distance(121, 599), 19)

    def test_2(self):
        self.assertEqual(digit_distance(12, 12), 0)

    def test_3(self):
        self.assertEqual(digit_distance(10, 20), 1)

    def test_4(self):
        self.assertEqual(digit_distance(12345678, 23456789), 8)

    def test_5(self):
        self.assertEqual(digit_distance(5555, 6666), 4)

    def test_6(self):
        self.assertEqual(digit_distance(105, 777), 15)


if __name__ == "__main__":
    unittest.main()