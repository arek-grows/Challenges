import unittest


def is_pandigital(number: int) -> bool:
    number = str(number)
    for xx in range(10):
        if str(xx) not in number:
            return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_pandigital(123456789876543210))

    def test_2(self):
        self.assertFalse(is_pandigital(546732965015))

    def test_3(self):
        self.assertTrue(is_pandigital(6781235184590))

    def test_4(self):
        self.assertTrue(is_pandigital(9432821089765))

    def test_5(self):
        self.assertFalse(is_pandigital(678798215643817))

    def test_6(self):
        self.assertFalse(is_pandigital(90864523148909))

    def test_7(self):
        self.assertFalse(is_pandigital(112233445566778899))

    def test_8(self):
        self.assertFalse(is_pandigital(647380265483206))

    def test_9(self):
        self.assertTrue(is_pandigital(38165975424790))

    def test_10(self):
        self.assertFalse(is_pandigital(8146327815320))


if __name__ == "__main__":
    unittest.main()