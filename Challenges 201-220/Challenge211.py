from __future__ import annotations
import unittest


def count_layers(rug: list[str]) -> int:
    center_idx = len(rug) // 2
    previous_pattern = ""
    layers = 0
    odd = 0
    if len(rug[center_idx]) % 2 == 1:
        odd = 1
    for i in rug[center_idx][0:(len(rug[center_idx]) // 2) + odd]:
        if i != previous_pattern:
            layers += 1
            previous_pattern = i
    return layers  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_layers(["AAA"]), 1)

    def test_2(self):
        self.assertEqual(count_layers(["AAAA", "AAAA", "AAAA"]), 1)

    def test_3(self):
        self.assertEqual(count_layers(["AAAA", "ABBA", "AAAA"]), 2)

    def test_4(self):
        self.assertEqual(
            count_layers(
                ["AAAAAAAAA", "ABBBBBBBA", "ABBBBBBBA", "ABBBBBBBA", "AAAAAAAAA"]
            ),
            2,
        )

    def test_5(self):
        self.assertEqual(
            count_layers(
                ["AAAAAAAAA", "ABBBBBBBA", "ABBAAABBA", "ABBBBBBBA", "AAAAAAAAA"]
            ),
            3,
        )

    def test_6(self):
        self.assertEqual(
            count_layers(
                ["AAAAAAAAA", "ABBBBBBBA", "ABCCCCCBA", "ABBBBBBBA", "AAAAAAAAA"]
            ),
            3,
        )

    def test_7(self):
        self.assertEqual(
            count_layers(
                [
                    "AAAAAAAAAAA",
                    "AABBBBBBBAA",
                    "AABCCCCCBAA",
                    "AABCAAACBAA",
                    "AABCADACBAA",
                    "AABCAAACBAA",
                    "AABCCCCCBAA",
                    "AABBBBBBBAA",
                    "AAAAAAAAAAA",
                ]
            ),
            5,
        )

    def test_8(self):
        self.assertEqual(
            count_layers(
                [
                    "AAAAAAAAAAA",
                    "AABBBBBBBAA",
                    "AABCCCCCBAA",
                    "AABCAAACBAA",
                    "AABCABACBAA",
                    "AABCAAACBAA",
                    "AABCCCCCBAA",
                    "AABBBBBBBAA",
                    "AAAAAAAAAAA",
                ]
            ),
            5,
        )

    def test_9(self):
        self.assertEqual(
            count_layers(
                [
                    "AAAAAAAAAAA",
                    "AABBBBBBBAA",
                    "AABCCCCCBAA",
                    "AABCDDDCBAA",
                    "AABCDDDCBAA",
                    "AABCDDDCBAA",
                    "AABCCCCCBAA",
                    "AABBBBBBBAA",
                    "AAAAAAAAAAA",
                ]
            ),
            4,
        )

    def test_10(self):
        self.assertEqual(
            count_layers(
                [
                    "FFFFFFFFFFFFFFFFFFFFFFFFF",
                    "FFFFFFFFFFFFFFFFFFFFFFFFF",
                    "FFFFGGGGGGGGGGGGGGGGGFFFF",
                    "FFFFGGGAAAAAAAAAAAGGGFFFF",
                    "FFFFGGGAABBBBBBBAAGGGFFFF",
                    "FFFFGGGAABCCCCCBAAGGGFFFF",
                    "FFFFGGGAABCDDDCBAAGGGFFFF",
                    "FFFFGGGAABCDDDCBAAGGGFFFF",
                    "FFFFGGGAABCDDDCBAAGGGFFFF",
                    "FFFFGGGAABCCCCCBAAGGGFFFF",
                    "FFFFGGGAABBBBBBBAAGGGFFFF",
                    "FFFFGGGAAAAAAAAAAAGGGFFFF",
                    "FFFFGGGGGGGGGGGGGGGGGFFFF",
                    "FFFFFFFFFFFFFFFFFFFFFFFFF",
                    "FFFFFFFFFFFFFFFFFFFFFFFFF",
                ]
            ),
            6,
        )


if __name__ == "__main__":
    unittest.main()