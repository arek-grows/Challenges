# Challenge 262 - Game of Sets
# In the game Set, three cards form a set if each of the cards are identical or
# completely different for each of the four properties. All three cards "must":
# - Have either the same color or different colors.
# - Have either the same number or different numbers.
# - Have either the same shades or different shades.
# - Have either the same shape or different shapes.
# The four properties "are":
# Colors: red, purple, green
# Numbers: 1, 2, 3
# Shades: empty, lined, full
# Shapes: squiggle, oval, diamond
# Here, a set is represented by a list containing three cards. Each card is represented by a dictionary of properties
# and values. Write a function  that determines whether three cards constitute a valid set.
# Here is an example of a "set": [
# { "color": "red", "number": 1, "shade": "empty", "shape": "squiggle" },
# { "color": "red", "number": 2, "shade": "lined", "shape": "diamond" },
# { "color": "red", "number": 3, "shade": "full", "shape": "oval" }
# ]
# "Same" "properties": color
# "Different" "properties": numbers, shading and shapes
# The following is not a "set": [
# { "color": "red", "number": 1, "shade": "empty", "shape": "squiggle" },
# { "color": "red", "number": 2, "shade": "lined", "shape": "diamond" },
# { "color": "purple", "number": 3, "shade": "full", "shape": "oval" }
# ]
# Colors are not all identical, but not all different.
# Examples
# isSet([
# { "color": "green", "number": 1, "shade": "empty", "shape": "squiggle" },
# { "color": "green", "number": 2, "shade": "empty", "shape": "diamond" },
# { "color": "green","number": 3, "shade": "empty", "shape": "oval" } ]) ➞ True
# isSet([
# { "color": "purple", "number": 1, "shade": "full", "shape": "oval" },
# { "color": "green", "number": 1, "shade": "full", "shape": "oval" },
# { "color": "red", "number": 1, "shade": "full", "shape": "oval" } ]) ➞ True
# isSet([
# { "color": "purple", "number": 3, "shade": "full", "shape": "oval" },
# { "color": "green", "number": 1, "shade": "full", "shape": "oval" },
# { "color": "red", "number": 3, "shade": "full", "shape": "oval" } ]) ➞ False
# Notes - A set cannot have 2/3 cards having the same property. Either all must share that property, or none will share
# that particular property.

from __future__ import annotations
import unittest


def is_set(cards: list) -> bool:
    properties = ['color', 'number', 'shade', 'shape']
    for p in properties:
        if cards[0][p] == cards[1][p] and cards[1][p] == cards[2][p]:
            pass
        elif cards[0][p] != cards[1][p] and cards[0][p] != cards[2][p] and cards[1][p] != cards[2][p]:
            pass
        else:
            return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self): self.assertFalse(is_set([{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
                                               {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
                                               {"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}, ]))

    def test_2(self): self.assertTrue(is_set([{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
                                              {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
                                              {"color": "red", "number": 1, "shade": "lined", "shape": "oval"}, ]))

    def test_3(self): self.assertFalse(is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
                                               {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
                                               {"color": "red", "number": 1, "shade": "lined", "shape": "oval"}, ]))

    def test_4(self): self.assertTrue(is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
                                              {"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
                                              {"color": "red", "number": 3, "shade": "full", "shape": "oval"}, ]))

    def test_5(self): self.assertTrue(is_set([{"color": "green", "number": 1, "shade": "empty", "shape": "squiggle"},
                                              {"color": "green", "number": 2, "shade": "empty", "shape": "diamond"},
                                              {"color": "green", "number": 3, "shade": "empty", "shape": "oval"}, ]))

    def test_6(self): self.assertTrue(is_set([{"color": "purple", "number": 1, "shade": "full", "shape": "oval"},
                                              {"color": "green", "number": 1, "shade": "full", "shape": "oval"},
                                              {"color": "red", "number": 1, "shade": "full", "shape": "oval"}, ]))

    def test_7(self): self.assertFalse(is_set([{"color": "purple", "number": 3, "shade": "full", "shape": "oval"},
                                               {"color": "green", "number": 1, "shade": "full", "shape": "oval"},
                                               {"color": "red", "number": 3, "shade": "full", "shape": "oval"}, ]))

    def test_8(self): self.assertFalse(is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
                                               {"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
                                               {"color": "purple", "number": 3, "shade": "full", "shape": "oval"}, ]))


if __name__ == "__main__":
    unittest.main()
