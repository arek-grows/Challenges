import unittest
from typing import List


def likes(users: List[str]) -> str:
    nr_users = len(users)
    who_liked = 'less than 0 people liked this!'
    if nr_users == 0:
        who_liked = "no one likes this"
    elif nr_users == 1:
        who_liked = "%s likes this" % (users[0])
    elif nr_users == 2:
        who_liked = "%s and %s like this" % (users[0], users[1])
    elif nr_users == 3:
        who_liked = "%s, %s and %s like this" % (users[0], users[1], users[2])
    elif nr_users > 3:
        who_liked = "%s, %s and %d others like this" % (users[0], users[1], nr_users - 2)
    return who_liked  # Put your code here!


class TestLikes(unittest.TestCase):
    def test_1(self):
        self.assertEqual('no one likes this', likes([]))

    def test_2(self):
        self.assertEqual('Peter likes this', likes(['Peter']))

    def test_3(self):
        self.assertEqual('Jacob and Alex like this', likes(['Jacob', 'Alex']))

    def test_4(self):
        self.assertEqual('Max, John and Mark like this', likes(['Max', 'John', 'Mark']))

    def test_5(self):
        self.assertEqual('Alex, Jacob and 2 others like this', likes(['Alex', 'Jacob', 'Mark', 'Max']))


if __name__ == "__main__":
    unittest.main()