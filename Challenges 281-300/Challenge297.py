import unittest


def is_heteromecic(number: int) -> bool:
    for x in range(number + 1):
        if x * (x + 1) == number:
            return True
        elif x * (x + 1) > number:
            return False


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_heteromecic(0))

    def test_2(self):
        self.assertTrue(is_heteromecic(2))

    def test_3(self):
        self.assertFalse(is_heteromecic(7))

    def test_4(self):
        self.assertTrue(is_heteromecic(110))

    def test_5(self):
        self.assertFalse(is_heteromecic(136))

    def test_6(self):
        self.assertTrue(is_heteromecic(156))

    def test_7(self):
        self.assertTrue(is_heteromecic(182))

    def test_8(self):
        self.assertFalse(is_heteromecic(218))

    def test_9(self):
        self.assertFalse(is_heteromecic(250))

    def test_10(self):
        self.assertTrue(is_heteromecic(272))


if __name__ == "__main__":
    unittest.main()