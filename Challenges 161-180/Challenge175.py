import unittest


def has_syncopation(music: str) -> bool:
    for i, beat in enumerate(music):
        if i % 2 != 0 and beat == '#':
            return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(has_syncopation(".#.#.#.#"), True)

    def test_2(self):
        self.assertEqual(has_syncopation("#.#...#."), False)

    def test_3(self):
        self.assertEqual(has_syncopation("#.#.###."), True)

    def test_4(self):
        self.assertEqual(has_syncopation(".."), False)

    def test_5(self):
        self.assertEqual(has_syncopation(""), False)

    def test_6(self):
        self.assertEqual(has_syncopation("##"), True)

    def test_7(self):
        self.assertEqual(has_syncopation("####...."), True)

    def test_8(self):
        self.assertEqual(has_syncopation("#"), False)

    def test_9(self):
        self.assertEqual(has_syncopation(".#.#...."), True)

    def test_10(self):
        self.assertEqual(has_syncopation(".#.#"), True)

    def test_11(self):
        self.assertEqual(has_syncopation(".#."), True)

    def test_12(self):
        self.assertEqual(has_syncopation("#."), False)

    def test_13(self):
        self.assertEqual(has_syncopation(".#"), True)


if __name__ == "__main__":
    unittest.main()