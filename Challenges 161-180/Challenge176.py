import unittest


def normalize(text: str) -> str:
    if text.isupper():
        text = text[0] + text[1:].lower() + '!'
    return text  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            normalize("CAPS LOCK DAY IS OVER"),
            "Caps lock day is over!",
        )

    def test_2(self):
        self.assertEqual(
            normalize("Today is not caps lock day."), "Today is not caps lock day."
        )

    def test_3(self):
        self.assertEqual(
            normalize("WE WANT THIS COVID THING TO BE OVER"),
            "We want this covid thing to be over!",
        )

    def test_4(self):
        self.assertEqual(
            normalize("Let us stay calm, no need to panic."),
            "Let us stay calm, no need to panic.",
        )

    def test_5(self):
        self.assertEqual(normalize("DO NOT SHOUT"), "Do not shout!")

    def test_6(self):
        self.assertEqual(
            normalize("Civilized conversation."), "Civilized conversation."
        )


if __name__ == "__main__":
    unittest.main()