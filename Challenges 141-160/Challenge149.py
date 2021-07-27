import unittest


def calculate_damage(damage: int, speed: int, duration: str) -> int:
    if damage < 0 or speed < 0:
        return "invalid"
    time_multiplier = {"second": 1, "minute": 60, "hour": 3600}
    return damage * speed * time_multiplier[duration]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(200, calculate_damage(40, 5, "second"))

    def test_2(self):
        self.assertEqual(6000, calculate_damage(100, 1, "minute"))

    def test_3(self):
        self.assertEqual(720000, calculate_damage(2, 100, "hour"))

    def test_4(self):
        self.assertEqual(600, calculate_damage(20, 0.5, "minute"))

    def test_5(self):
        self.assertEqual(2880000, calculate_damage(2, 400, "hour"))

    def test_6(self):
        self.assertEqual("invalid", calculate_damage(-23, 20, "second"))

    def test_7(self):
        self.assertEqual("invalid", calculate_damage(-23, -5, "second"))

    def test_8(self):
        self.assertEqual("invalid", calculate_damage(20, -492321, "hour"))


if __name__ == "__main__":
    unittest.main()