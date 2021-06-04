import unittest


def nb_year(p0: int, percent: float, aug: int, p: int) -> int:
    years_counter = 0
    while p0 <= p:
        p0 = p0*(1+(percent*0.01)) + aug
        p0 = int(p0)
        years_counter += 1
    return years_counter  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)

    def test_2(self):
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)

    def test_3(self):
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)


if __name__ == "__main__":
    unittest.main()