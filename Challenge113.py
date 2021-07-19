import unittest


def cap_to_front(string: str) -> str:
    string = list(string)
    end = []
    index = 0
    for s in string:
        if s.isupper():
            end.insert(index, s)
            index += 1
        else:
            end.append(s)
    return "".join(end)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("APhpy", cap_to_front("hApPy"))

    def test_2(self):
        self.assertEqual("MENTmove", cap_to_front("moveMENT"))

    def test_3(self):
        self.assertEqual("PPEal", cap_to_front("aPPlE"))

    def test_4(self):
        self.assertEqual("OCAKEshrt", cap_to_front("shOrtCAKE"))


if __name__ == "__main__":
    unittest.main()