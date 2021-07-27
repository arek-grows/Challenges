import inspect
import unittest


def emphasize(string: str) -> str:
    words = string.split()
    end_list = []
    for word in words:
        capitalized_word = ""
        first_index = True

        for w in word:
            if not first_index:
                if w.isalpha():
                    capitalized_word += w.lower()
                else:
                    capitalized_word += w
            else:
                if w.isalpha():
                    capitalized_word += w.upper()
                else:
                    capitalized_word += w
                first_index = False

        end_list.append(capitalized_word)
    return " ".join(end_list)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(emphasize("hello world"), "Hello World")

    def test_2(self):
        self.assertEqual(emphasize("GOOD MORNING"), "Good Morning")

    def test_3(self):
        self.assertEqual(emphasize("99 red balloons!"), "99 Red Balloons!")

    def test_4(self):
        self.assertEqual(emphasize("1 2 3 4 5 6 7 8 9"), "1 2 3 4 5 6 7 8 9")

    def test_5(self):
        self.assertEqual(emphasize(""), "")

    def test_6(self):
        self.assertEqual(emphasize("joshua senoron"), "Joshua Senoron")

    def test_7(self):
        self.assertNotEqual(str.title, emphasize)
        self.assertNotIn(".title", inspect.getsource(emphasize))


if __name__ == "__main__":
    unittest.main()