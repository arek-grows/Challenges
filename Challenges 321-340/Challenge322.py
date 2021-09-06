import unittest


def dakiti(string: str) -> str:
    string = string.split()
    end_string = [""] * len(string)
    for ss in string:
        for cc in ss:
            if cc.isdigit():
                end_string[int(cc) - 1] = ss.replace(cc, "")
                break
    return " ".join(end_string)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves"),
            "baby ya yo me entere se nota cuando me-ves",
        )

    def test_2(self):
        self.assertEqual(
            dakiti("h4as don2de ah1i n3o ll5egado q7ue 8yo te9-llevare s6abes"),
            "ahi donde no has llegado sabes que yo te-llevare",
        )

    def test_3(self):
        self.assertEqual(
            dakiti("quie3res bebe4r dime1 e5s qu6e qu2e tu7 er8es m9i-bebe"),
            "dime que quieres beber es que tu eres mi-bebe",
        )

    def test_4(self):
        self.assertEqual(
            dakiti("y1 de2 nos3tros qu4ien v5a a6 h7ablar 8si 9no"),
            "y de nostros quien va a hablar si no",
        )

    def test_5(self):
        self.assertEqual(dakiti("no1 n2os v4er de3jamos"), "no nos dejamos ver")


if __name__ == "__main__":
    unittest.main()