import unittest
from typing import List


def calculate_score(*rounds: List[str]) -> str:
    scores = {"Abigail": 0, "Benson": 0, "Tie": 0}
    rps = ["R", "P", "S"]
    rps_matrix = [["Tie", "Benson", "Abigail"], ["Abigail", "Tie", "Benson"], ["Benson", "Abigail", "Tie"]]
    for rnd in rounds:
        scores[rps_matrix[rps.index(rnd[0])][rps.index(rnd[1])]] += 1
    if scores["Abigail"] == scores["Benson"]:
        return "Tie"
    else:
        return max(scores, key=scores.get)


class TestRockPaperScissors(unittest.TestCase):
    def test_game_1(self):
        self.assertEqual("Abigail", calculate_score(["R", "P"], ["R", "S"], ["S", "P"]))

    def test_game_2(self):
        self.assertEqual("Tie", calculate_score(["R", "R"], ["S", "S"]))

    def test_game_3(self):
        self.assertEqual("Tie", calculate_score(["S", "R"], ["R", "S"], ["R", "R"]))

    def test_game_4(self):
        self.assertEqual("Tie", calculate_score(["S", "R"], ["P", "R"]))

    def test_game_5(self):
        self.assertEqual(
            "Abigail",
            calculate_score(["S", "S"], ["S", "P"], ["R", "S"], ["S", "R"], ["R", "R"])
        )

    def test_game_6(self):
        self.assertEqual(
            "Benson",
            calculate_score(["S", "R"], ["S", "R"], ["S", "R"], ["R", "S"], ["R", "S"])
        )


if __name__ == "__main__":
    unittest.main()