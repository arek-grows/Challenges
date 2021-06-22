import unittest


def get_nth_tetrahedral(n: int) -> int:
    return (n * (n + 1) * (n + 2)) / 6  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_nth_tetrahedral(1), 1)

    def test_2(self):
        self.assertEqual(get_nth_tetrahedral(2), 4)

    def test_3(self):
        self.assertEqual(get_nth_tetrahedral(3), 10)

    def test_4(self):
        self.assertEqual(get_nth_tetrahedral(4), 20)

    def test_5(self):
        self.assertEqual(get_nth_tetrahedral(5), 35)

    def test_6(self):
        self.assertEqual(get_nth_tetrahedral(9), 165)


if __name__ == "__main__":
    unittest.main()