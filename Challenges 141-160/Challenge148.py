from __future__ import annotations
import unittest


def calc_uncovered(stolen_items: dict[str, int], coverage_limit: int) -> int:
    stolen_value = 0
    for item in stolen_items:
        stolen_value += stolen_items[item]
    covered = stolen_value - coverage_limit
    if covered < 0:
        return 0
    return covered  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(25001, calc_uncovered({"skate": 20000, "painting": 30000, "shoes": 1}, 25000))

    def test_2(self):
        self.assertEqual(11, calc_uncovered({"baseball bat": 31}, 20))

    def test_3(self):
        self.assertEqual(0, calc_uncovered({"stereo": 1110, "pillow": 25}, 5000))


if __name__ == "__main__":
    unittest.main()