import unittest


def greeting(name: str) -> str:
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    if name not in GUEST_LIST:
        return "Hi! I'm a guest."
    else:
        return "Hi! I'm %s, and I'm from %s." % (name, GUEST_LIST[name])  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(greeting("Randy"), "Hi! I'm Randy, and I'm from Germany.")

    def test_2(self):
        self.assertEqual(greeting("Sam"), "Hi! I'm Sam, and I'm from Argentina.")

    def test_3(self):
        self.assertEqual(greeting("Monti"), "Hi! I'm a guest.")

    def test_4(self):
        self.assertEqual(greeting("Trudy"), "Hi! I'm a guest.")

    def test_5(self):
        self.assertEqual(greeting("Wendy"), "Hi! I'm Wendy, and I'm from Japan.")


if __name__ == "__main__":
    unittest.main()