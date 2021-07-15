import unittest
import random


def roll_dice(dice_rolls: str) -> str:
    totals = []
    dice_rolls = dice_rolls.split()
    rolls_list = []

    for rolling in dice_rolls:
        rolls_list.append(rolling.split('d'))
    for rolling in rolls_list:
        total = 0
        for x in range(int(rolling[0])):
            total += random.randrange(1, int(rolling[1]) + 1)
        totals.append(str(total))
    return "\n".join(totals)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        for i in range(1000):
            rolls = roll_dice("1d6")
            roll = int(rolls.strip())
            assert 1 <= roll <= 6

    def test_2(self):
        for i in range(1000):
            rolls = roll_dice("1d20")
            roll = int(rolls.strip())
            assert 1 <= roll <= 20

    def test_3(self):
        for i in range(1000):
            rolls = roll_dice("1d6\n1d12")
            for sides, roll in zip((6, 12), map(int, rolls.split())):
                assert 1 <= roll <= sides

    def test_4(self):
        for i in range(1000):
            rolls = roll_dice("10d6")
            roll = int(rolls.strip())
            assert 10 <= roll <= 60

    def test_5(self):
        for i in range(1000):
            rolls = roll_dice("10d6\n10d12")
            for sides, roll in zip((6, 12), map(int, rolls.split())):
                assert 10 <= roll <= sides * 10

    def test_6(self):
        count = {f"{i+1}": 0 for i in range(1, 10)}
        for i in range(10000):
            rolls = roll_dice("2d5")
            count[rolls] += 1
        least_common = min(count.items(), key=lambda item: item[1])
        self.assertLess(100, least_common[1], f"Your algorithm never returned a roll sum of {least_common[0]}")


if __name__ == "__main__":
    unittest.main()
