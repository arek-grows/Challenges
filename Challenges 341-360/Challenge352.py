import unittest


def staircase(steps: int) -> str:
    reverse = False
    if steps < 0:
        reverse = True
        steps *= -1

    stairs = []
    unders = steps - 1
    hashes = 1
    for xx in range(steps):
        stairs.append(("_" * unders) + ("#" * hashes))
        unders -= 1
        hashes += 1
    if reverse:
        stairs = stairs[::-1]
    return "\n".join(stairs)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(staircase(3), "__#\n_##\n###")

    def test_2(self):
        self.assertEqual(
            staircase(7),
            "______#\n_____##\n____###\n___####\n__#####\n_######\n#######",
        )

    def test_3(self):
        self.assertEqual(staircase(2), "_#\n##")

    def test_4(self):
        self.assertEqual(
            staircase(-8),
            "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#",
        )

    def test_5(self):
        self.assertEqual(staircase(4), "___#\n__##\n_###\n####")

    def test_6(self):
        self.assertEqual(
            staircase(-12),
            "############\n_###########\n__##########\n___#########\n____########\n_____#######\n______######\n_______#####\n________####\n_________###\n__________##\n___________#",
        )

    def test_7(self):
        self.assertEqual(
            staircase(11),
            "__________#\n_________##\n________###\n_______####\n______#####\n_____######\n____#######\n___########\n__#########\n_##########\n###########",
        )

    def test_8(self):
        self.assertEqual(
            staircase(-6), "######\n_#####\n__####\n___###\n____##\n_____#"
        )


if __name__ == "__main__":
    unittest.main()
