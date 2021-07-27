from __future__ import annotations
import unittest


def construct_deconstruct(string: str) -> list[str]:
    end_list = []
    for x in range(1, len(string) + 1):
        end_list.append(string[0:x])
    for x in range(len(string) - 1, 0, -1):
        end_list.append(string[0:x])
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            construct_deconstruct("Hello"),
            ["H", "He", "Hel", "Hell", "Hello", "Hell", "Hel", "He", "H"],
        )

    def test_2(self):
        self.assertListEqual(
            construct_deconstruct("edabit"),
            [
                "e",
                "ed",
                "eda",
                "edab",
                "edabi",
                "edabit",
                "edabi",
                "edab",
                "eda",
                "ed",
                "e",
            ],
        )

    def test_3(self):
        self.assertListEqual(
            construct_deconstruct("the sun"),
            [
                "t",
                "th",
                "the",
                "the ",
                "the s",
                "the su",
                "the sun",
                "the su",
                "the s",
                "the ",
                "the",
                "th",
                "t",
            ],
        )

    def test_8(self):
        self.assertListEqual(construct_deconstruct(""), [])

    def test_9(self):
        self.assertListEqual(
            construct_deconstruct("        "),
            [
                " ",
                "  ",
                "   ",
                "    ",
                "     ",
                "      ",
                "       ",
                "        ",
                "       ",
                "      ",
                "     ",
                "    ",
                "   ",
                "  ",
                " ",
            ],
        )


if __name__ == "__main__":
    unittest.main()