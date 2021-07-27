import unittest


def apocalyptic(number: int) -> str:
    doomsday = str(2 ** number)
    if "666" in doomsday:
        return "Repent! %s days until the Apocalypse!" % doomsday.index("666")
    return "Crisis averted. Resume sinning."  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Repent! 9 days until the Apocalypse!", apocalyptic(157))

    def test_2(self):
        self.assertEqual("Crisis averted. Resume sinning.", apocalyptic(175))

    def test_3(self):
        self.assertEqual("Repent! 6 days until the Apocalypse!", apocalyptic(220))

    def test_4(self):
        self.assertEqual("Crisis averted. Resume sinning.", apocalyptic(333))

    def test_5(self):
        self.assertEqual("Repent! 138 days until the Apocalypse!", apocalyptic(499))

    def test_6(self):
        self.assertEqual("Repent! 49 days until the Apocalypse!", apocalyptic(666))

    def test_7(self):
        self.assertEqual("Crisis averted. Resume sinning.", apocalyptic(1003))


if __name__ == "__main__":
    unittest.main()