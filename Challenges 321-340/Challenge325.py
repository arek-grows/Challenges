import unittest


def calc_bundled_temp(layers: int, temperature: str) -> str:
    temp = int(temperature[:temperature.index("*")])
    for ii in range(layers):
        temp *= 1.1
    return f"{temp:.1f}*C"  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calc_bundled_temp(2, "10*C"), "12.1*C")

    def test_2(self):
        self.assertEqual(calc_bundled_temp(1, "2*C"), "2.2*C")

    def test_3(self):
        self.assertEqual(calc_bundled_temp(4, "6*C"), "8.8*C")

    def test_4(self):
        self.assertEqual(calc_bundled_temp(20, "4*C"), "26.9*C")

    def test_5(self):
        self.assertEqual(calc_bundled_temp(5, "20*C"), "32.2*C")

    def test_6(self):
        self.assertEqual(calc_bundled_temp(20, "3*C"), "20.2*C")

    def test_7(self):
        self.assertEqual(calc_bundled_temp(5, "18*C"), "29.0*C")

    def test_8(self):
        self.assertEqual(calc_bundled_temp(4, "5*C"), "7.3*C")

    def test_9(self):
        self.assertEqual(calc_bundled_temp(16, "17*C"), "78.1*C")

    def test_10(self):
        self.assertEqual(calc_bundled_temp(15, "2*C"), "8.4*C")


if __name__ == "__main__":
    unittest.main()