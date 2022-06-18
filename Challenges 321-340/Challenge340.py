from __future__ import annotations
import unittest


def batting_avg(numbers: list[list[int]]) -> str:
    total_hits = 0
    total_at_bats = 0
    for nn in numbers:
        total_hits += nn[0]
        total_at_bats += nn[1]
    BA = round(total_hits / total_at_bats, 3)
    BA = str(BA)[1:]
    if len(BA) != 4:
        BA += "0" * (4 - len(BA))
    return BA  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(batting_avg([[0, 0], [1, 3], [2, 2], [0, 4], [1, 5],]), ".286")

    def test_2(self):
        self.assertEqual(batting_avg([[2, 5], [2, 3], [0, 3], [1, 5], [2, 4],]), ".350")

    def test_3(self):
        self.assertEqual(batting_avg([[2, 3], [1, 5], [2, 4], [1, 5], [0, 5],]), ".273")

    def test_4(self):
        self.assertEqual(batting_avg([[1, 4], [0, 5], [4, 4], [1, 5], [0, 5],]), ".261")

    def test_5(self):
        self.assertEqual(batting_avg([[3, 3], [0, 5], [0, 4], [3, 5], [1, 5],]), ".318")


if __name__ == "__main__":
    unittest.main()