import unittest


def correct_spacing(sentence: str) -> str:
    return " ".join(sentence.split())  # Put your code here!!!


class TestCorrectSpaces(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            "A glittering gem is not enough.",
            correct_spacing(" A  glittering  gem     is    not   enough.  "),
        )

    def test_2(self):
        self.assertEqual(
            "She did her best to help him.",
            correct_spacing("   She      did  her best  to  help    him.  "),
        )

    def test_3(self):
        self.assertEqual(
            "They made sure to get there early.",
            correct_spacing("  They      made  sure   to get   there  early. "),
        )

    def test_4(self):
        self.assertEqual(
            "She did her best to help him.",
            correct_spacing("  She  did   her      best     to   help him. "),
        )

    def test_5(self):
        self.assertEqual(
            "I love eating toasted cheese and tuna sandwiches.",
            correct_spacing(
                "      I     love  eating    toasted  cheese   and tuna  sandwiches."
            ),
        )

    def test_6(self):
        self.assertEqual(
            "There were foggy conditions on the trail.",
            correct_spacing(
                "  There     were  foggy   conditions on   the      trail.   "
            ),
        )

    def test_7(self):
        self.assertEqual(
            "The roads were impassable due to snow.",
            correct_spacing("     The  roads   were  impassable  due to      snow.  "),
        )

    def test_8(self):
        self.assertEqual(
            "Better to paint with bold colors.",
            correct_spacing(" Better   to      paint  with  bold  colors.   "),
        )

    def test_9(self):
        self.assertEqual(
            "Remember to stretch before you run.",
            correct_spacing("     Remember to  stretch      before you  run.  "),
        )


if __name__ == "__main__":
    unittest.main()