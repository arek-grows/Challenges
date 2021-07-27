import unittest


def format_time(seconds: int) -> str:
    if seconds == 0:
        return "00:00:00"
    time = [seconds // 3600]
    seconds -= time[0] * 3600
    time.append(seconds//60)
    seconds -= time[1] * 60
    time.append(seconds)
    time = [str(x) for x in time]
    for x, t in enumerate(time):
        if len(t) == 1:
            time[x] = '0' + t
    return ":".join(time)  # Put your code here!!!


class TestFormatTime(unittest.TestCase):
    def test_1(self):
        self.assertEqual("00:00:00", format_time(0))

    def test_2(self):
        self.assertEqual("00:00:05", format_time(5))

    def test_3(self):
        self.assertEqual("00:01:00", format_time(60))

    def test_4(self):
        self.assertEqual("23:59:59", format_time(86399))

    def test_5(self):
        self.assertEqual("99:59:59", format_time(359999))


if __name__ == "__main__":
    unittest.main()