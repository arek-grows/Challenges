import unittest


def cap_last(string: str) -> str:
    string = string.split()
    end_string = []
    for word in string:
        end_string.append(word[:len(word) - 1] + word[-1].upper())
    return " ".join(end_string)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cap_last("hello"), "hellO")

    def test_2(self):
        self.assertEqual(cap_last("My Name Is Beginner Codes"), "MY NamE IS BeginneR CodeS")

    def test_3(self):
        self.assertEqual(
            cap_last("HELp THe LASt LETTERs CAPITALISe"),
            "HELP THE LAST LETTERS CAPITALISE",
        )

    def test_4(self):
        self.assertEqual(cap_last("hellooooo"), "hellooooO")

    def test_5(self):
        self.assertEqual(
            cap_last("hahA I aM alreadY capitaliseD"), "hahA I aM alreadY capitaliseD"
        )


if __name__ == "__main__":
    unittest.main()