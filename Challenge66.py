import unittest
from typing import List


def in_box(box: List[str]) -> bool:
    return False  # Put your code here!!!


class TestInBox(unittest.TestCase):
    def test_1(self):
        self.assertFalse(in_box(["###", "# #", "###"]))

    def test_2(self):
        self.assertFalse(in_box(["####", "#  #", "#  #", "####"]))

    def test_3(self):
        self.assertFalse(in_box(["#####", "#   #", "#   #", "#   #", "#####"]))

    def test_4(self):
        self.assertTrue(in_box(["###", "#*#", "###"]))

    def test_5(self):
        self.assertTrue(in_box(["####", "# *#", "#  #", "####"]))

    def test_6(self):
        self.assertTrue(in_box(["#####", "#  *#", "#   #", "#   #", "#####"]))

    def test_7(self):
        self.assertTrue(in_box(["#####", "#   #", "# * #", "#   #", "#####"]))

    def test_8(self):
        self.assertTrue(in_box(["#####", "#   #", "#   #", "# * #", "#####"]))

    def test_9(self):
        self.assertTrue(in_box(["#####", "#*  #", "#   #", "#   #", "#####"]))


if __name__ == "__main__":
    unittest.main()