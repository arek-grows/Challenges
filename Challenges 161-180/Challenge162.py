from __future__ import annotations
import unittest


def havel_hakimi(already_met: list[int]) -> bool:
    while True:
        [already_met.remove(0) for x in range(already_met.count(0))]
        if len(already_met) == 0:
            return True
        already_met.sort()
        already_met = already_met[::-1]
        N = already_met.pop(0)
        if N > len(already_met):
            return False
        for x in range(N):
            already_met[x] = already_met[x] - 1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))

    def test_2(self):
        self.assertFalse(havel_hakimi([4, 2, 0, 1, 5, 0]))

    def test_3(self):
        self.assertTrue(havel_hakimi([3, 1, 2, 3, 1, 0]))

    def test_4(self):
        self.assertTrue(
            havel_hakimi(
                [16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
            )
        )

    def test_5(self):
        self.assertTrue(
            havel_hakimi(
                [14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]
            )
        )

    def test_6(self):
        self.assertFalse(
            havel_hakimi(
                [15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]
            )
        )

    def test_7(self):
        self.assertFalse(
            havel_hakimi(
                [6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]
            )
        )

    def test_8(self):
        self.assertFalse(havel_hakimi([2, 2, 0]))

    def test_9(self):
        self.assertFalse(havel_hakimi([3, 2, 1]))

    def test_10(self):
        self.assertTrue(havel_hakimi([1, 1]))

    def test_11(self):
        self.assertFalse(havel_hakimi([1]))

    def test_12(self):
        self.assertTrue(havel_hakimi([]))


if __name__ == "__main__":
    unittest.main()