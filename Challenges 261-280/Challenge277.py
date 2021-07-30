from __future__ import annotations
import unittest


def distance_to_nearest_vowel(string: str) -> list[int]:
    end_list = []
    vowels = "aeiou"
    vowel_idxs = []
    for i, s in enumerate(string):
        if s in vowels:
            vowel_idxs.append(i)
    for i, s in enumerate(string):
        if i not in vowel_idxs:
            if len(vowel_idxs) == 1:
                end_list.append(abs(vowel_idxs[0] - i))
            else:
                lowest = abs(vowel_idxs[0] - i)
                for vi in vowel_idxs[1:]:
                    if abs(vi - i) < lowest:
                        lowest = abs(vi - i)
                    else:
                        break
                end_list.append(lowest)
        else:
            end_list.append(0)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(distance_to_nearest_vowel("aaaaa"), [0, 0, 0, 0, 0])

    def test_2(self):
        self.assertListEqual(distance_to_nearest_vowel("bba"), [2, 1, 0])

    def test_3(self):
        self.assertListEqual(distance_to_nearest_vowel("abbb"), [0, 1, 2, 3])

    def test_4(self):
        self.assertListEqual(distance_to_nearest_vowel("abab"), [0, 1, 0, 1])

    def test_5(self):
        self.assertListEqual(distance_to_nearest_vowel("babbb"), [1, 0, 1, 2, 3])

    def test_6(self):
        self.assertListEqual(distance_to_nearest_vowel("baaab"), [1, 0, 0, 0, 1])

    def test_7(self):
        self.assertListEqual(
            distance_to_nearest_vowel("abcdabcd"), [0, 1, 2, 1, 0, 1, 2, 3]
        )

    def test_8(self):
        self.assertListEqual(
            distance_to_nearest_vowel("abbaaaaba"), [0, 1, 1, 0, 0, 0, 0, 1, 0]
        )

    def test_9(self):
        self.assertListEqual(
            distance_to_nearest_vowel("treesandflowers"),
            [2, 1, 0, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 2],
        )

    def test_10(self):
        self.assertListEqual(
            distance_to_nearest_vowel("pokerface"), [1, 0, 1, 0, 1, 1, 0, 1, 0]
        )

    def test_11(self):
        self.assertListEqual(
            distance_to_nearest_vowel("beautiful"), [1, 0, 0, 0, 1, 0, 1, 0, 1]
        )

    def test_12(self):
        self.assertListEqual(
            distance_to_nearest_vowel("rythmandblues"),
            [5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 0, 1],
        )

    def test_13(self):
        self.assertListEqual(
            distance_to_nearest_vowel("shopper"), [2, 1, 0, 1, 1, 0, 1]
        )

    def test_14(self):
        self.assertListEqual(
            distance_to_nearest_vowel("singingintherain"),
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1],
        )

    def test_15(self):
        self.assertListEqual(
            distance_to_nearest_vowel("sugarandspice"),
            [1, 0, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0],
        )

    def test_16(self):
        self.assertListEqual(
            distance_to_nearest_vowel("totally"), [1, 0, 1, 0, 1, 2, 3]
        )


if __name__ == "__main__":
    unittest.main()