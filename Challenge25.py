import unittest
from typing import AnyStr, List


def route_difference(directions: List[AnyStr]) -> int:
    nr_directions = [directions.count("N"),
                     directions.count("S"),
                     directions.count("E"),
                     directions.count("W")]
    cancelled = abs(nr_directions[0] - nr_directions[1]) + abs(nr_directions[2] - nr_directions[3])
    return len(directions) - cancelled  # Put your code here!


class TestDirectionallyChallenged(unittest.TestCase):
    def test_1(self):
        self.assertEqual(route_difference(['N', 'E', 'S', 'W']), 4)

    def test_2(self):
        self.assertEqual(route_difference(['N', 'N', 'N', 'E', 'N', 'E']), 0)

    def test_3(self):
        self.assertEqual(route_difference(['N', 'S', 'N', 'S', 'E', 'W', 'E', 'E']), 6)

    def test_4(self):
        self.assertEqual(route_difference(['N', 'S', 'N', 'S', 'E']), 4)

    def test_5(self):
        self.assertEqual(route_difference(['N', 'N', 'S', 'S', 'S', 'S', 'E']), 4)

    def test_6(self):
        self.assertEqual(route_difference(['N', 'N', 'S', 'S', 'W', 'S', 'E']), 6)

    def test_7(self):
        self.assertEqual(route_difference(['N', 'S', 'E']), 2)

    def test_8(self):
        self.assertEqual(route_difference(['S', 'S', 'S']), 0)

    def test_9(self):
        self.assertEqual(route_difference(['S', 'S', 'S', 'S', 'S', 'N']), 2)


if __name__ == "__main__":
    unittest.main()