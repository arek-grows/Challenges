# Challenge 218 - Pluralize!
#
# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
# Examples
#
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#
# pluralize(["table", "table", "table"]) ➞ { "tables" }
#
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
#
# Notes
#
#     This is an oversimplification of the English language so no edge cases will appear.
#     Only focus on whether to add an s to the ends of the words.


from __future__ import annotations
import unittest


def pluralize(things: list[str]) -> set[str]:
    already = []
    pluralized = []
    for thing in things:
        if things.count(thing) > 1 and thing not in already:
            already.append(thing)
            pluralized.append(thing + 's')
        elif thing not in already:
            pluralized.append(thing)
    return set(pluralized)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pluralize(["cow", "pig", "cow", "cow"]), {"cows", "pig"})

    def test_2(self):
        self.assertEqual(pluralize(["table", "table", "table"]), {"tables"})

    def test_3(self):
        self.assertEqual(
            pluralize(["chair", "pencil", "arm"]), {"chair", "pencil", "arm"}
        )

    def test_4(self):
        self.assertEqual(pluralize(["list"]), {"list"})

    def test_5(self):
        self.assertEqual(
            pluralize(
                [
                    "set",
                    "set",
                    "tuple",
                    "tuple",
                    "string",
                    "string",
                    "string",
                    "string",
                    "integer",
                ]
            ),
            {"sets", "tuples", "strings", "integer"},
        )


if __name__ == "__main__":
    unittest.main()