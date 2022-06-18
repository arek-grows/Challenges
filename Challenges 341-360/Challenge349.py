import unittest


def remove_repeats(string: str) -> str:
    end_string = ""
    previous_letter = ""
    for ss in string:
        if ss != previous_letter:
            end_string += ss
            previous_letter = ss
    return end_string  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(remove_repeats("aaabbbccc"), "abc")

    def test_2(self):
        self.assertEqual(remove_repeats("bookkeeper"), "bokeper")

    def test_3(self):
        self.assertEqual(remove_repeats("nananana"), "nananana")

    def test_4(self):
        self.assertEqual(
            remove_repeats("accddbccabadcabccdababaacbdaadcccbcaabaaddbabbaadd"),
            "acdbcabadcabcdababacbdadcbcabadbabad",
        )

    def test_5(self):
        self.assertEqual(
            remove_repeats("aabbcabdcddddacdccacbbcabadccbbaadcccbddacbdbabbbd"),
            "abcabdcdacdcacbcabadcbadcbdacbdbabd",
        )

    def test_6(self):
        self.assertEqual(
            remove_repeats("dacbaabacbabacabcabaabdccccbdbbcaadddacdbdbdacbada"),
            "dacbabacbabacabcababdcbdbcadacdbdbdacbada",
        )

    def test_7(self):
        self.assertEqual(
            remove_repeats("cbdbcbcccbdbbcaaaacacbcabddcdcddcccbdaabdacbdcabbd"),
            "cbdbcbcbdbcacacbcabdcdcdcbdabdacbdcabd",
        )

    def test_8(self):
        self.assertEqual(
            remove_repeats("cdbdcdccccbcbbcdabbbbcababccadccabdcacabbcaccdaccd"),
            "cdbdcdcbcbcdabcababcadcabdcacabcacdacd",
        )

    def test_9(self):
        self.assertEqual(
            remove_repeats("bacbdbdadbbbdacbddbdcbadddabbaadcbbdabdaabcdddbacd"),
            "bacbdbdadbdacbdbdcbadabadcbdabdabcdbacd",
        )

    def test_10(self):
        self.assertEqual(
            remove_repeats("daadadccbcacacbacdbbaabaadbaabadacdacadbacdcababbb"),
            "dadadcbcacacbacdbabadbabadacdacadbacdcabab",
        )


if __name__ == "__main__":
    unittest.main()