import unittest


def does_brick_fit(width: int, height: int, depth: int, hole_width: int, hole_height: int) -> bool:
    hole_size = hole_height * hole_width
    if (width * height <= hole_size) or (width * depth <= hole_size) or (height * depth <= hole_size):
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(does_brick_fit(1, 1, 1, 1, 1))

    def test_2(self):
        self.assertTrue(does_brick_fit(1, 2, 1, 1, 1))

    def test_3(self):
        self.assertFalse(does_brick_fit(1, 2, 2, 1, 1))

    def test_4(self):
        self.assertTrue(does_brick_fit(1, 2, 2, 1, 2))

    def test_5(self):
        self.assertTrue(does_brick_fit(1, 2, 2, 2, 1))

    def test_6(self):
        self.assertFalse(does_brick_fit(2, 2, 2, 1, 2))


if __name__ == "__main__":
    unittest.main()
