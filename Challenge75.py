import unittest
from typing import List


def score(throw: List[int]) -> int:
    total = 0
    triples = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    singles = {1: 100, 5: 50}
    for t in triples:
        total += throw.count(t) // 3 * triples[t]
    for s in singles:
        total += throw.count(s) % 3 * singles[s]
    return total  # Put your code here!!!


class TestScore(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, score([2, 3, 4, 6, 2]))

    def test_2(self):
        self.assertEqual(400, score([4, 4, 4, 3, 3]))

    def test_3(self):
        self.assertEqual(450, score([2, 4, 4, 5, 4]))


if __name__ == "__main__":
    unittest.main()