import unittest


def space_weights(planet_a: str, weight: float, planet_b: str) -> float:
    g_force = {"Mercury": 3.7, "Venus": 8.87, "Earth": 9.81, "Mars": 3.711, "Jupiter": 24.79, "Saturn": 10.44,
               "Uranus": 8.69, "Neptune": 11.15}
    return round(weight / g_force[planet_a] * g_force[planet_b], 2)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0.38, space_weights("Earth", 1, "Mars"))

    def test_2(self):
        self.assertEqual(2.53, space_weights("Earth", 1, "Jupiter"))

    def test_3(self):
        self.assertEqual(1.14, space_weights("Earth", 1, "Neptune"))

    def test_4(self):
        self.assertEqual(14.93, space_weights("Jupiter", 100, "Mercury"))

    def test_5(self):
        self.assertEqual(209.61, space_weights("Venus", 75, "Jupiter"))

    def test_6(self):
        self.assertEqual(12.01, space_weights("Uranus", 10, "Saturn"))

    def test_7(self):
        self.assertEqual(119.64, space_weights("Mars", 120, "Mercury"))

    def test_8(self):
        self.assertEqual(1250.23, space_weights("Neptune", 1421, "Earth"))

    def test_9(self):
        self.assertEqual(4.93, space_weights("Jupiter", 33, "Mercury"))

    def test_10(self):
        self.assertEqual(471.54, space_weights("Saturn", 555, "Venus"))

    def test_11(self):
        self.assertEqual(1.24, space_weights("Jupiter", 3.141592, "Earth"))


if __name__ == "__main__":
    unittest.main()