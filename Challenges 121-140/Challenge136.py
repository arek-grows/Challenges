from __future__ import annotations
import unittest
import math


def spin_around(turns: list[str]) -> int:
    rights = turns.count("right")
    lefts = turns.count("left")
    turns = math.floor(abs((rights * 0.25) + (lefts * 0.25 * -1)))
    # if turns < 1:
    #     turns = 0
    return turns  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, spin_around(["left", "right", "left", "right"]))

    def test_2(self):
        self.assertEqual(
            2,
            spin_around(
                ["right", "right", "right", "right", "right", "right", "right", "right"]
            ),
        )

    def test_3(self):
        self.assertEqual(1, spin_around(["left", "left", "left", "left"]))

    def test_4(self):
        self.assertEqual(0, spin_around([]))

    def test_5(self):
        self.assertEqual(0, spin_around(["left"]))

    def test_6(self):
        self.assertEqual(0, spin_around(["right"]))

    def test_7(self):
        self.assertEqual(
            1, spin_around(["right", "right", "right", "left", "right", "right"])
        )

    def test_8(self):
        self.assertEqual(
            1,
            spin_around(
                [
                    "left",
                    "left",
                    "right",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "right",
                    "left",
                    "left",
                    "right",
                    "right",
                    "right",
                    "right",
                    "left",
                    "left",
                    "right",
                    "right",
                ]
            ),
        )

    def test_9(self):
        self.assertEqual(
            0,
            spin_around(
                [
                    "right",
                    "left",
                    "left",
                    "right",
                    "left",
                    "left",
                    "right",
                    "left",
                    "right",
                    "right",
                    "left",
                    "left",
                    "right",
                    "right",
                    "right",
                    "left",
                    "left",
                    "right",
                ]
            ),
        )

    def test_10(self):
        self.assertEqual(
            10,
            spin_around(
                [
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                    "right",
                ]
            ),
        )

    def test_11(self):
        self.assertEqual(
            10,
            spin_around(
                [
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                    "left",
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()