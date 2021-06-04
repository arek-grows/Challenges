# Challenge 226 - Get Free Wi-Fi Anywhere You Go
#
# A new 'hacky' phone is launched, which has the feature of connecting to any Wi-Fi network from any distance away, as long as there aren't any obstructions between the hotspot and the phone. Given a string, return how many Wi-Fi hotspots I'm able to connect to.
#
#     The phone is represented as a P.
#     A hotspot is represented as an *.
#     An obstruction is represented as a #.
#
# You cannot access a hotspot if it is behind an obstruction.
# Examples
#
# nonstop_hotspot("*   P  *   *") ➞ 3
#
# nonstop_hotspot("*  * #  * P # * #") ➞ 1
#
# nonstop_hotspot("***#P#***") ➞ 0
#
# Notes
#
#     There will be only one phone.
#     No other characters, other than spaces, will appear in the tests.


import unittest


def nonstop_hotspot(area: str) -> int:
    hotspots = 0
    for x in area.split('#'):
        if 'P' in x:
            hotspots = x.count('*')
    return hotspots  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nonstop_hotspot("*   P  *   *"), 3)

    def test_2(self):
        self.assertEqual(nonstop_hotspot("*  * #  * P # * #"), 1)

    def test_3(self):
        self.assertEqual(nonstop_hotspot("***#P#***"), 0)

    def test_4(self):
        self.assertEqual(nonstop_hotspot("#P#"), 0)

    def test_5(self):
        self.assertEqual(nonstop_hotspot("P"), 0)

    def test_6(self):
        self.assertEqual(nonstop_hotspot("P       #"), 0)

    def test_7(self):
        self.assertEqual(nonstop_hotspot("P     *  # *"), 1)

    def test_8(self):
        self.assertEqual(nonstop_hotspot("*   # * P"), 1)

    def test_9(self):
        self.assertEqual(nonstop_hotspot("# *****  **  P     ** #    "), 9)


if __name__ == "__main__":
    unittest.main()
