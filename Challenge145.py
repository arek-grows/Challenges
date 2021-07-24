import unittest


def get_check_digit(upc: int) -> int:
    upc = [int(x) for x in str(upc)]
    if len(upc) < 11:
        for x in range(11 - len(upc)):
            upc.insert(0, 0)

    end = 0
    for i in upc[0::2]:
        end += i
    end *= 3
    for i in upc[1::2]:
        end += i
    end = end % 10
    if end == 0:
        return 0
    return 10 - end  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, get_check_digit(4210000526))

    def test_2(self):
        self.assertEqual(2, get_check_digit(3600029145))

    def test_3(self):
        self.assertEqual(4, get_check_digit(12345678910))

    def test_4(self):
        self.assertEqual(0, get_check_digit(1234567))


if __name__ == "__main__":
    unittest.main()