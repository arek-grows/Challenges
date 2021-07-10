import unittest
from typing import List


def ping_pong(pings: List[str], win: bool) -> List[str]:
    p_p = ['Ping!', "Pong!"]
    end = p_p * len(pings)
    if not win:
        end.pop(-1)
    return end  # Put your code here!!!


class TestPingPong(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"],
            ping_pong(["Ping!", "Ping!", "Ping!"], True),
        )

    def test_2(self):
        self.assertEqual(
            ["Ping!", "Pong!", "Ping!"], ping_pong(["Ping!", "Ping!"], False)
        )

    def test_3(self):
        self.assertEqual(["Ping!", "Pong!"], ping_pong(["Ping!"], True))


if __name__ == "__main__":
    unittest.main()