import unittest


def calculate_damage(your_type: str, opponents_type: str, your_atk: int, opponents_atk: int) -> int:
    effectiveness_dict = {"fire": {"water": 0.5, "grass": 2},
                          "water": {"grass": 0.5, "electric": 0.5, "fire": 2},
                          "grass": {"fire": 0.5, "water": 2},
                          "electric": {"water": 2}}
    effectiveness = 1
    if your_type in effectiveness_dict and opponents_type in effectiveness_dict[your_type]:
        effectiveness = effectiveness_dict[your_type][opponents_type]
    return 50 * (your_atk/opponents_atk) * effectiveness  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(25, calculate_damage("fire", "water", 100, 100))

    def test_2(self):
        self.assertEqual(100, calculate_damage("grass", "water", 100, 100))

    def test_3(self):
        self.assertEqual(50, calculate_damage("electric", "fire", 100, 100))

    def test_4(self):
        self.assertEqual(150, calculate_damage("grass", "electric", 57, 19))

    def test_5(self):
        self.assertEqual(100, calculate_damage("grass", "water", 40, 40))

    def test_6(self):
        self.assertEqual(175, calculate_damage("grass", "fire", 35, 5))

    def test_7(self):
        self.assertEqual(250, calculate_damage("fire", "electric", 10, 2))


if __name__ == "__main__":
    unittest.main()