import unittest

hacker_dict = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5'
}


def hacker_speak(text: str) -> str:
    output = ''
    for c in text:
        if c in hacker_dict:
            output += hacker_dict[c]
        else:
            output += c
    return output  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hacker_speak("javascript is cool"), "j4v45cr1pt 15 c00l")

    def test_2(self):
        self.assertEqual(hacker_speak("become a coder"), "b3c0m3 4 c0d3r")

    def test_3(self):
        self.assertEqual(hacker_speak("hi there"), "h1 th3r3")

    def test_4(self):
        self.assertEqual(hacker_speak("programming is fun"), "pr0gr4mm1ng 15 fun")

    def test_5(self):
        self.assertEqual(hacker_speak("keep on practicing"), "k33p 0n pr4ct1c1ng")


if __name__ == "__main__":
    unittest.main()