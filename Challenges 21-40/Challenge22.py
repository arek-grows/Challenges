import unittest
from typing import AnyStr, List


def transform_upvotes(upvotes: AnyStr) -> List[int]:
    upvotes = upvotes.split()
    end_list = []
    for vote in upvotes:
        if 'k' in vote:
            end_list.append(float(vote[:vote.index('k')])*1000)
        else:
            end_list.append(int(vote))
    return end_list


class TestsUpvotes(unittest.TestCase):
    def test_1(self):
        self.assertEqual(transform_upvotes('20.3k 3.8k 7.7k 992'), [20300, 3800, 7700, 992])

    def test_2(self):
        self.assertEqual(transform_upvotes('5.5k 8.9k 32'), [5500, 8900, 32])

    def test_3(self):
        self.assertEqual(transform_upvotes('6.8k 13.5k'), [6800, 13500])


if __name__ == "__main__":
    unittest.main()