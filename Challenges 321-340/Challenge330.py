import unittest


def double_swap(string: str, character_1: str, character_2: str) -> str:
    end_string = ""
    for cc in string:
        if cc is character_1:
            end_string += character_2
        elif cc is character_2:
            end_string += character_1
        else:
            end_string += cc
    return end_string  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(double_swap("aabbccc", "a", "b"), "bbaaccc")

    def test_2(self):
        self.assertEqual(double_swap("random w#rds writt&n h&r&", "#", "&"), "random w&rds writt#n h#r#")

    def test_3(self):
        self.assertEqual(double_swap("128 895 556 788 999", "8", "9"), "129 985 556 799 888")

    def test_4(self):
        self.assertEqual(double_swap("mamma mia", "m", "a"), "amaam aim")

    def test_5(self):
        self.assertEqual(double_swap("**##**", "*", "#"), "##**##")

    def test_6(self):
        self.assertEqual(double_swap("123456789", "4", "5"), "123546789")

    def test_7(self):
        self.assertEqual(double_swap("445566&&", "4", "&"), "&&556644")

    def test_8(self):
        self.assertEqual(double_swap("!?@,.", ",", "."), "!?@.,")

    def test_9(self):
        self.assertEqual(double_swap("Q_Q T_T =.= >.<", "Q", "T"), "T_T Q_Q =.= >.<")

    def test_10(self):
        self.assertEqual(double_swap("(Q_Q) (T_T) (=.=) (>.<)", ")", "("), ")Q_Q( )T_T( )=.=( )>.<(")

    def test_11(self):
        self.assertEqual(double_swap("<>", ">", "<"), "><")

    def test_12(self):
        self.assertEqual(double_swap("001101", "1", "0"), "110010")

    def test_13(self):
        self.assertEqual(double_swap("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~", "a", "b"), "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`bacdefghijklmnopqrstuvwxyz{|}~")


if __name__ == "__main__":
    unittest.main()