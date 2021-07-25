from __future__ import annotations
import unittest


def character_mapping(string: str) -> list[int]:
    accounted_for = []
    end_map = []
    for s in string:
        if s not in accounted_for:
            accounted_for.append(s)
        end_map.append(accounted_for.index(s))
    return end_map  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(character_mapping("abcd"), [0, 1, 2, 3])

    def test_2(self):
        self.assertListEqual(character_mapping("abb"), [0, 1, 1])

    def test_3(self):
        self.assertListEqual(character_mapping("babbcb"), [0, 1, 0, 0, 2, 0])

    def test_4(self):
        self.assertListEqual(character_mapping("aaabb"), [0, 0, 0, 1, 1])

    def test_5(self):
        self.assertListEqual(character_mapping("abccbc"), [0, 1, 2, 2, 1, 2])

    def test_6(self):
        self.assertListEqual(character_mapping("fluffy"), [0, 1, 2, 0, 0, 3])

    def test_7(self):
        self.assertListEqual(character_mapping("madness"), [0, 1, 2, 3, 4, 5, 5])

    def test_8(self):
        self.assertListEqual(character_mapping("buttery"), [0, 1, 2, 2, 3, 4, 5])

    def test_9(self):
        self.assertListEqual(character_mapping("canine"), [0, 1, 2, 3, 2, 4])

    def test_10(self):
        self.assertListEqual(character_mapping("hohoho"), [0, 1, 0, 1, 0, 1])

    def test_11(self):
        self.assertListEqual(character_mapping("hmmmmm"), [0, 1, 1, 1, 1, 1])

    def test_12(self):
        self.assertListEqual(character_mapping(""), [])


if __name__ == "__main__":
    unittest.main()