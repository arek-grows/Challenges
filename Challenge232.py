import unittest


def compare_longest(current, longest):
    if len(current) > len(longest):
        longest = current
    return longest


def longest_substring(string: str) -> str:
    previous_num = ''
    c_sub = ''
    l_sub = ''

    for x in string:
        if int(x) % 2 == 0 and previous_num == 'odd':  # even, p odd
            c_sub += x
            previous_num = 'even'
        elif int(x) % 2 == 0 and previous_num == 'even':  # even, p even
            c_sub = x
        elif previous_num == 'odd':  # odd, p odd
            c_sub = x
        elif previous_num == 'even':  # odd, p even
            c_sub += x
            previous_num = 'odd'
        else:
            if int(x) % 2 == 0:
                previous_num = 'even'
            else:
                previous_num = 'odd'
            c_sub = x
        l_sub = compare_longest(c_sub, l_sub)
    return l_sub  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            longest_substring("844929328912985315632725682153"), "56327256"
        )

    def test_2(self):
        self.assertEqual(
            longest_substring("769697538272129475593767931733"), "27212947"
        )

    def test_3(self):
        self.assertEqual(longest_substring("937948289456111258444958189244"), "894561")

    def test_4(self):
        self.assertEqual(longest_substring("736237766362158694825822899262"), "636")

    def test_5(self):
        self.assertEqual(longest_substring("369715978955362655737322836233"), "369")

    def test_6(self):
        self.assertEqual(longest_substring("345724969853525333273796592356"), "496985")

    def test_7(self):
        self.assertEqual(longest_substring("548915548581127334254139969136"), "8581")

    def test_8(self):
        self.assertEqual(longest_substring("417922164857852157775176959188"), "78521")

    def test_9(self):
        self.assertEqual(longest_substring("251346385699223913113161144327"), "638569")

    def test_10(self):
        self.assertEqual(longest_substring("483563951878576456268539849244"), "18785")

    def test_11(self):
        self.assertEqual(longest_substring("853667717122615664748443484823"), "474")

    def test_12(self):
        self.assertEqual(longest_substring("398785511683322662883368457392"), "98785")

    def test_13(self):
        self.assertEqual(longest_substring("368293545763611759335443678239"), "76361")

    def test_14(self):
        self.assertEqual(longest_substring("775195358448494712934755311372"), "4947")

    def test_15(self):
        self.assertEqual(longest_substring("646113733929969155976523363762"), "76523")

    def test_16(self):
        self.assertEqual(longest_substring("575337321726324966478369152265"), "478369")

    def test_17(self):
        self.assertEqual(longest_substring("754388489999793138912431545258"), "545258")

    def test_18(self):
        self.assertEqual(
            longest_substring("198644286258141856918653955964"), "2581418569"
        )

    def test_19(self):
        self.assertEqual(longest_substring("643349187319779695864213682274"), "349")

    def test_20(self):
        self.assertEqual(longest_substring("919331281193713636178478295857"), "36361")


if __name__ == "__main__":
    unittest.main()