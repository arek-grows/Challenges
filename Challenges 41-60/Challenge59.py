import unittest
from typing import List


def check_flush(table: List[str], hand: List[str]) -> bool:
    suits = ['S', 'H', 'D', 'C']
    suit_count = [0, 0, 0, 0]
    for t in table:
        suit_count[suits.index(t[-1])] += 1
    for h in hand:
        suit_count[suits.index(h[-1])] += 1
    for counts in suit_count:
        if counts >= 5:
            return True
    return False  # Put your code here!!!


class TestCheckFlush(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_flush(['A_S', 'J_H', '7_D', '8_D', '10_D'], ['J_D', '3_D']))

    def test_2(self):
        self.assertTrue(check_flush(['10_S', '7_S', '9_H', '4_S', '3_S'], ['K_S', 'Q_S']))

    def test_3(self):
        self.assertFalse(check_flush(['3_S', '10_H', '10_D', '10_C', '10_S'], ['3_S', '4_D']))

    def test_4(self):
        self.assertFalse(check_flush(['8_H', '10_H', '10_D', 'J_H', '10_S'], ['5_D', 'Q_H']))


if __name__ == "__main__":
    unittest.main()