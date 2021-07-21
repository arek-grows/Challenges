import unittest


def worm_length(worm: str) -> str:
    if len(worm) == worm.count('-') and len(worm) != 0:
        return "%s mm." % (len(worm) * 10)
    return "invalid"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("100 mm.", worm_length("----------"))

    def test_2(self):
        self.assertEqual("invalid", worm_length(""))

    def test_3(self):
        self.assertEqual("invalid", worm_length("---_-___---_"))

    def test_4(self):
        self.assertEqual("60 mm.", worm_length("------"))

    def test_5(self):
        self.assertEqual("invalid", worm_length("iwheguawhpvpaiehpiuwwega"))

    def test_6(self):
        self.assertEqual("invalid", worm_length("QWERTYUIOPASDFGHJKL"))

    def test_7(self):
        self.assertEqual("120 mm.", worm_length("------------"))


if __name__ == "__main__":
    unittest.main()