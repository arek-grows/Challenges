import unittest


def possible_bonus(your_position: int, friends_position: int) -> bool:
    if (your_position < friends_position) and (your_position + 6 >= friends_position):
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(possible_bonus(3, 7))

    def test_2(self):
        self.assertTrue(possible_bonus(0, 6))

    def test_3(self):
        self.assertTrue(possible_bonus(1, 6))

    def test_4(self):
        self.assertTrue(possible_bonus(2, 6))

    def test_5(self):
        self.assertTrue(possible_bonus(3, 6))

    def test_6(self):
        self.assertTrue(possible_bonus(4, 6))

    def test_7(self):
        self.assertTrue(possible_bonus(5, 6))

    def test_8(self):
        self.assertFalse(possible_bonus(6, 6))

    def test_9(self):
        self.assertFalse(possible_bonus(7, 6))

    def test_10(self):
        self.assertTrue(possible_bonus(23, 27))

    def test_11(self):
        self.assertFalse(possible_bonus(1, 9))

    def test_12(self):
        self.assertFalse(possible_bonus(5, 3))


if __name__ == "__main__":
    unittest.main()