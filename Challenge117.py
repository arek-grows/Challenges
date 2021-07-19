import unittest


def vow_replace(phrase: str, substitute: str) -> str:
    vowels = 'aeiou'
    end = ''
    for p in phrase:
        if p in vowels:
            p = substitute
        end += p
    return end  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("upplus und bununus", vow_replace("apples and bananas", "u"))

    def test_2(self):
        self.assertEqual("chooso cossorolo", vow_replace("cheese casserole", "o"))

    def test_3(self):
        self.assertEqual("steffed jelepene peppers", vow_replace("stuffed jalapeno poppers", "e"))

    def test_4(self):
        self.assertEqual("shramp tampara", vow_replace("shrimp tempura", "a"))

    def test_5(self):
        self.assertEqual("tini sishimi", vow_replace("tuna sashimi", "i"))

    def test_6(self):
        self.assertEqual("chacalata caka", vow_replace("chocolate cake", "a"))


if __name__ == "__main__":
    unittest.main()