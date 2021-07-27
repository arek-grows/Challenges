import unittest


def is_triplet(a: int, b: int, c: int) -> bool:
    nr_list = [a ** 2, b ** 2, c ** 2]
    highest = max(nr_list)
    nr_list.remove(highest)
    if nr_list[0] + nr_list[1] == highest:
        return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_triplet(3, 4, 5))

    def test_2(self):
        self.assertFalse(is_triplet(1, 2, 3))

    def test_3(self):
        self.assertFalse(is_triplet(3, 18, 8))

    def test_4(self):
        self.assertFalse(is_triplet(7, 12, 7))

    def test_5(self):
        self.assertTrue(is_triplet(13, 5, 12))

    def test_6(self):
        self.assertFalse(is_triplet(12, 20, 18))

    def test_7(self):
        self.assertFalse(is_triplet(17, 14, 2))

    def test_8(self):
        self.assertFalse(is_triplet(6, 15, 12))

    def test_9(self):
        self.assertTrue(is_triplet(60, 61, 11))

    def test_10(self):
        self.assertFalse(is_triplet(7, 13, 15))


if __name__ == "__main__":
    unittest.main()