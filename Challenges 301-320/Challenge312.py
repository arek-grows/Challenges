import unittest


class Composer:
    count: int  # Put your code here!!!
    count = 0

    def __init__(self, name, year, place):
        Composer.count += 1
        self.name = name
        self.year = year
        self.place = place


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Composer.count, 0)

    def test_2(self):
        c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
        self.assertEqual(Composer.count, 1)

    def test_3(self):
        c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
        c3 = Composer("Johannes Brahms", 1833, "Germany")
        self.assertEqual(Composer.count, 3)

    def test_4(self):
        c4 = Composer("Richard Wagner", 1813, "Germany")
        c5 = Composer("Claude Debussy", 1862, "France")
        c6 = Composer("Richard Tchaikovsky", 1840, "Russia")
        c7 = Composer("Frederic Chopin", 1810, "Poland")
        self.assertEqual(Composer.count, 7)

    def test_5(self):
        c8 = Composer("Joseph Haydn", 1732, "Austria")
        self.assertEqual(Composer.count, 8)


if __name__ == "__main__":
    unittest.main()