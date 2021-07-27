from __future__ import annotations
import unittest


def color_invert(color: tuple[int, int, int]) -> tuple[int, int, int]:
    return abs(color[0] - 255), abs(color[1] - 255), abs(color[2] - 255)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual((90, 85, 136), color_invert((165, 170, 119)))

    def test_2(self):
        self.assertEqual((90, 85, 119), color_invert((165, 170, 136)))

    def test_3(self):
        self.assertEqual((90, 85, 102), color_invert((165, 170, 153)))

    def test_4(self):
        self.assertEqual((90, 85, 85), color_invert((165, 170, 170)))

    def test_5(self):
        self.assertEqual((90, 85, 68), color_invert((165, 170, 187)))

    def test_6(self):
        self.assertEqual((90, 85, 51), color_invert((165, 170, 204)))

    def test_7(self):
        self.assertEqual((90, 85, 34), color_invert((165, 170, 221)))

    def test_8(self):
        self.assertEqual((90, 85, 17), color_invert((165, 170, 238)))

    def test_9(self):
        self.assertEqual((90, 75, 255), color_invert((165, 180, 0)))

    def test_10(self):
        self.assertEqual((90, 75, 238), color_invert((165, 180, 17)))

    def test_11(self):
        self.assertEqual((90, 75, 221), color_invert((165, 180, 34)))

    def test_12(self):
        self.assertEqual((90, 75, 204), color_invert((165, 180, 51)))

    def test_13(self):
        self.assertEqual((90, 75, 187), color_invert((165, 180, 68)))

    def test_14(self):
        self.assertEqual((90, 75, 170), color_invert((165, 180, 85)))

    def test_15(self):
        self.assertEqual((90, 75, 153), color_invert((165, 180, 102)))

    def test_16(self):
        self.assertEqual((255, 255, 255), color_invert((0, 0, 0)))

    def test_17(self):
        self.assertEqual((255, 255, 238), color_invert((0, 0, 17)))

    def test_18(self):
        self.assertEqual((255, 255, 221), color_invert((0, 0, 34)))

    def test_19(self):
        self.assertEqual((255, 255, 204), color_invert((0, 0, 51)))

    def test_20(self):
        self.assertEqual((255, 255, 187), color_invert((0, 0, 68)))


if __name__ == "__main__":
    unittest.main()