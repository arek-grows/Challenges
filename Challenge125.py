import unittest


def minutes_to_seconds(time_string: str) -> int:
    times = time_string.split(":")
    if int(times[1]) >= 60:
        return False
    return int(times[0]) * 60 + int(times[1])  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(60, minutes_to_seconds("01:00"))

    def test_2(self):
        self.assertEqual(836, minutes_to_seconds("13:56"))

    def test_3(self):
        self.assertEqual(False, minutes_to_seconds("10:60"))

    def test_4(self):
        self.assertEqual(7941, minutes_to_seconds("132:21"))

    def test_5(self):
        self.assertEqual(False, minutes_to_seconds("132:271"))

    def test_6(self):
        self.assertEqual(90, minutes_to_seconds("01:30"))

    def test_7(self):
        self.assertEqual(600, minutes_to_seconds("10:00"))


if __name__ == "__main__":
    unittest.main()