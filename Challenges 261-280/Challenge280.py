from __future__ import annotations
import unittest


def pairs(sequence: list[int]) -> list[list[int]]:
    odd = False
    if len(sequence) % 2 != 0:
        odd = sequence.pop(len(sequence) // 2)
    first_half = sequence[0:len(sequence) // 2]
    second_half = sequence[::-1]
    second_half = second_half[0:len(sequence) // 2]
    end = []
    for a, b in zip(first_half, second_half):
        end.append([a, b])
    if odd:
        end.append([odd, odd])
    return end  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(pairs([1, 2, 3, 4, 5, 6, 7]), [[1, 7], [2, 6], [3, 5], [4, 4]])

    def test_2(self):
        self.assertListEqual(pairs([1, 2, 3, 4, 5, 6]), [[1, 6], [2, 5], [3, 4]])

    def test_3(self):
        self.assertListEqual(pairs([5, 9, 8, 1, 2]), [[5, 2], [9, 1], [8, 8]])

    def test_4(self):
        self.assertListEqual(pairs([1, 1, 4, 4, 5, 5]), [[1, 5], [1, 5], [4, 4]])

    def test_5(self):
        self.assertListEqual(pairs([9, 9, 9, 9, 3, 3, 9]), [[9, 9], [9, 3], [9, 3], [9, 9]])

    def test_6(self):
        self.assertListEqual(pairs([5, 6, 7]), [[5, 7], [6, 6]])

    def test_7(self):
        self.assertListEqual(pairs([5, 6]), [[5, 6]])

    def test_8(self):
        self.assertListEqual(pairs([5]), [[5, 5]])

    def test_9(self):
        self.assertListEqual(pairs([]), [])


if __name__ == "__main__":
    unittest.main()