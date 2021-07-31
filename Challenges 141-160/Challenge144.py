import unittest


def total_distance(height: float, length: float, tower_height: float) -> float:
    return round(tower_height + (tower_height / height * length), 1)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(300.0, total_distance(0.2, 0.4, 100.0))

    def test_2(self):
        self.assertEqual(18.3, total_distance(0.12, 0.1, 10.0))

    def test_3(self):
        self.assertEqual(50.0, total_distance(0.5, 0.5, 25.0))

    def test_4(self):
        self.assertEqual(12.0, total_distance(0.1, 0.1, 6.0))

    def test_5(self):
        self.assertEqual(3.3, total_distance(0.05, 0.1, 1.1))

    def test_6(self):
        self.assertEqual(1554.0, total_distance(1.0, 1.0, 777.0))

    def test_7(self):
        self.assertEqual(150.9, total_distance(0.2, 0.1, 100.6))


if __name__ == "__main__":
    unittest.main()