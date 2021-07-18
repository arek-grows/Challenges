import unittest


def showdown(p1: str, p2: str) -> str:
    if p1.index("Bang!") == p2.index("Bang!"):
        return "tie"
    else:
        winners = {p1.index("Bang!"): "p1", p2.index("Bang!"): "p2"}
        return winners[min(winners)]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("p1", showdown("   Bang!        ", "        Bang!   "))

    def test_2(self):
        self.assertEqual("p2", showdown("               Bang! ", "             Bang!   "))

    def test_3(self):
        self.assertEqual("p2", showdown("  Bang!   ", "Bang!     "))

    def test_4(self):
        self.assertEqual("tie", showdown("     Bang!   ", "     Bang!   "))

    def test_5(self):
        self.assertEqual("p1", showdown("  Bang!     ", "     Bang!  "))

    def test_6(self):
        self.assertEqual("p1", showdown(" Bang!  ", "  Bang! "))

    def test_7(self):
        self.assertEqual("p2", showdown("          Bang!       ", "       Bang!          "))

    def test_8(self):
        self.assertEqual("tie", showdown("    Bang!    ", "    Bang!    "))

    def test_9(self):
        self.assertEqual("tie", showdown("       Bang!       ", "       Bang!       "))

    def test_10(self):
        self.assertEqual("p1", showdown(" Bang!      ", "      Bang! "))


if __name__ == "__main__":
    unittest.main()