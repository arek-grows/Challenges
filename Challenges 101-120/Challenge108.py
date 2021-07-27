import unittest


def how_many_times(message: str) -> int:
    # ord('a') == 97, ord('b') == 98
    presses = 0
    for m in message:
        presses += ord(m.lower()) - 96
    return presses  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(123, how_many_times("qudusayo"))

    def test_2(self):
        self.assertEqual(43, how_many_times("que"))

    def test_3(self):
        self.assertEqual(7, how_many_times("abd"))


if __name__ == "__main__":
    unittest.main()