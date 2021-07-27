import unittest


def apply_potions(potions: str) -> str:
    end_string = ''
    p_num = ''
    for n in potions:
        if n == 'A':
            # grow
            end_string += str(int(p_num) + 1)
            p_num = ''
        elif n == 'B':
            # shrink
            end_string += str(int(p_num) - 1)
            p_num = ''
        else:
            p_num += n
    return end_string + p_num  # Replace with your own code!!!


class TestPotions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(apply_potions("567"), "567")

    def test_2(self):
        self.assertEqual(apply_potions("3A78B51"), "47751")

    def test_3(self):
        self.assertEqual(apply_potions("9999B"), "9998")

    def test_4(self):
        self.assertEqual(apply_potions("9A123"), "10123")

    def test_5(self):
        self.assertEqual(apply_potions("1A2A3A4A"), "2345")

    def test_6(self):
        self.assertEqual(apply_potions("9B8B7B6A"), "8767")

    def test_7(self):
        self.assertEqual(apply_potions("19A10B99A1000B"), "209100999")


if __name__ == "__main__":
    unittest.main()