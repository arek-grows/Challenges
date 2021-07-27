from __future__ import annotations
import unittest


def can_build(words: list[str]) -> bool:
    for i in range(0, len(words) - 1):
        if words[i] not in words[i + 1] or len(words[i]) + 1 != len(words[i + 1]):
            return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(can_build(["a", "at", "ate", "late", "plate", "plates"]))

    def test_2(self):
        self.assertFalse(can_build(["a", "at", "ate", "late", "plate", "plater", "platter"]))

    def test_3(self):
        self.assertTrue(can_build(["a", "ka", "ika", "pika", "pikac", "pikach", "pikachu"]))

    def test_4(self):
        self.assertFalse(can_build(["e", "tea", "teac", "teach", "teache", "teacher", "teachers"]))

    def test_5(self):
        self.assertTrue(can_build(["a", "at", "tat", "stat", "state", "estate", "estates"]))

    def test_6(self):
        self.assertFalse(can_build(["m", "ma", "man", "many", "meany"]))

    def test_7(self):
        self.assertTrue(can_build(["o", "ol", "old", "bold", "bolde", "mbolde", "embolde", "embolden"]))

    def test_8(self):
        self.assertFalse(can_build(["o", "op", "top", "stop", "stops", "stoops"]))

    def test_9(self):
        self.assertTrue(can_build(["mean", "meany"]))

    def test_10(self):
        self.assertFalse(can_build(["air", "air", "airy", "fairy"]))


if __name__ == "__main__":
    unittest.main()