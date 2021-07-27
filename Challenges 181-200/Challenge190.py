# Challenge 190 - Stalactites or Stalagmites?
#
# Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.
#
# Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.
# Examples
#
# mineral_formation([
#   [0, 1, 0, 1],
#   [0, 1, 0, 1],
#   [0, 0, 0, 1],
#   [0, 0, 0, 0]
# ]) ➞ "stalactites"
#
# mineral_formation([
#   [0, 0, 0, 0],
#   [0, 1, 0, 1],
#   [0, 1, 1, 1],
#   [0, 1, 1, 1]
# ]) ➞ "stalagmites"
#
# mineral_formation([
#   [1, 0, 1, 0],
#   [1, 1, 0, 1],
#   [0, 1, 1, 1],
#   [0, 1, 1, 1]
# ]) ➞ "both"
#
# Notes
#
#     There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
#     There won't be any example of neither stalactites or stalagmites.


from __future__ import annotations
import unittest


def mineral_formation(cave: list[list[int]]) -> str:
    if 1 in cave[0] and 1 in cave[len(cave)-1]:
        return 'both'
    elif 1 in cave[0]:
        return 'stalactites'
    elif 1 in cave[len(cave)-1]:
        return 'stalagmites'


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            mineral_formation([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]),
            "stalactites",
        )

    def test_2(self):
        self.assertEqual(
            mineral_formation([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]),
            "stalagmites",
        )

    def test_3(self):
        self.assertEqual(
            mineral_formation([[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]),
            "both",
        )

    def test_4(self):
        self.assertEqual(mineral_formation([[1], [1], [0], [0]]), "stalactites")

    def test_5(self):
        self.assertEqual(mineral_formation([[1], [1], [0], [1]]), "both")

    def test_6(self):
        self.assertEqual(mineral_formation([[0], [1], [1], [1]]), "stalagmites")

    def test_7(self):
        self.assertEqual(mineral_formation([[0, 1], [1, 1], [1, 1], [1, 0]]), "both")

    def test_8(self):
        self.assertEqual(mineral_formation([[0, 0], [1, 1],]), "stalagmites")

    def test_9(self):
        self.assertEqual(mineral_formation([[1, 1], [0, 0],]), "stalactites")


if __name__ == "__main__":
    unittest.main()