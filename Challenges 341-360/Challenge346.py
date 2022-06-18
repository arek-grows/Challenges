from __future__ import annotations
import unittest


def calculate_arrowhead(cards: list[str]) -> str:
    total = 0
    for mm in cards:
        total += mm.count(">")
        total -= mm.count("<")
    if total > 0:
        return ">" * total
    elif total < 0:
        return "<" * (total * -1)
    else:
        return ""  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calculate_arrowhead([">>>>", "<", "<", "<"]), ">")

    def test_2(self):
        self.assertEqual(calculate_arrowhead([">", "<", ">>", "<", "<<<"]), "<<")

    def test_3(self):
        self.assertEqual(calculate_arrowhead([">>>", "<<<"]), "")

    def test_4(self):
        self.assertEqual(calculate_arrowhead([">>", "<<", "<<<"]), "<<<")

    def test_5(self):
        self.assertEqual(
            calculate_arrowhead(
                [">", ">>>>>", ">>>>", ">>>>>>>", ">>>>>>>>", ">>>>", ">>>>>>>>"]
            ),
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
        )

    def test_6(self):
        self.assertEqual(
            calculate_arrowhead(
                ["<", ">>>>>>", "<<<<<<<<", "<<<<<<<<<<", ">>>>>>>", ">>>"]
            ),
            "<<<",
        )

    def test_7(self):
        self.assertEqual(calculate_arrowhead(["<<<<", ">>>>>"]), ">")

    def test_8(self):
        self.assertEqual(
            calculate_arrowhead(
                ["<<<<<<<<<", "<<<<", ">>>", ">>>>>>>>", ">>>>>>>", "<<<<<"]
            ),
            "",
        )

    def test_9(self):
        self.assertEqual(
            calculate_arrowhead([">>>>>>>>>>", "<<", ">>>>>>>>>>"]),
            ">>>>>>>>>>>>>>>>>>",
        )

    def test_10(self):
        self.assertEqual(
            calculate_arrowhead([">", "<<<", ">>>>>>>>>>", ">>>>>"]), ">>>>>>>>>>>>>"
        )


if __name__ == "__main__":
    unittest.main()