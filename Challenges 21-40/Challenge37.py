import unittest
from typing import Any, List


def match_last_item(items: List[Any]) -> bool:
    items = map(str, items)
    items = list(items)
    if items[-1] == "".join(items[:len(items) - 1]):
        return True
    return False  # Put your code here!!!


class TestMatchLastItem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(match_last_item(['rsq', '6hi', 'g', 'rsq6hig']), True)

    def test_2(self):
        self.assertEqual(match_last_item([0, 1, 2, 3, 4, 5, '12345']), False)

    def test_3(self):
        self.assertEqual(match_last_item(['for', 'mi', 'da', 'bel', 'formidable']), False)

    def test_4(self):
        self.assertEqual(match_last_item([8, 'thunder', True, '8thunderTrue']), True)

    def test_5(self):
        self.assertEqual(match_last_item([ 1, 1, 1, '11' ]), False)

    def test_6(self):
        self.assertEqual(match_last_item(['tocto','G8G','xtohkgc','3V8','ctyghrs',100.88,'fyuo','Q','toctoG8Gxtohkgc3V8ctyghrs100.88fyuoQ']), True)


if __name__ == "__main__":
    unittest.main()