import unittest


def sort_it(unsorted_list: list) -> list:
    end_list = []
    list_list = []
    for i in unsorted_list:
        if type(i) == list:
            end_list.append(i[0])
            list_list.append(i[0])
        else:
            end_list.append(i)
    end_list.sort()
    for i in list_list:
        end_list[end_list.index(i)] = [i]
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sort_it([4, 1, 3]), [1, 3, 4])

    def test_2(self):
        self.assertEqual(sort_it([[4], [1], [3]]), [[1], [3], [4]])

    def test_3(self):
        self.assertEqual(sort_it([4, [1], 3]), [[1], 3, 4])

    def test_4(self):
        self.assertEqual(sort_it([[4], 1, [3]]), [1, [3], [4]])

    def test_5(self):
        self.assertEqual(sort_it([[3], 4, [2], [5], 1, 6]), [1, [2], [3], 4, [5], 6])

    def test_6(self):
        self.assertEqual(sort_it([[3], 7, [9], [5], 1, 6]), [1, [3], [5], 6, 7, [9]])

    def test_7(self):
        self.assertEqual(
            sort_it([[3], 7, [9], [5], 1, 6, [0]]), [[0], 1, [3], [5], 6, 7, [9]]
        )


if __name__ == "__main__":
    unittest.main()