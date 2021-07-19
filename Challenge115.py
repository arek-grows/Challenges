import unittest


def relation_to_luke(name: str) -> str:
    lukes_relations = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    if name in lukes_relations:
        return lukes_relations[name]
    return "not aquainted"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("father", relation_to_luke("Darth Vader"))

    def test_2(self):
        self.assertEqual("sister", relation_to_luke("Leia"))

    def test_3(self):
        self.assertEqual("brother in law", relation_to_luke("Han"))

    def test_4(self):
        self.assertEqual("droid", relation_to_luke("R2D2"))


if __name__ == "__main__":
    unittest.main()