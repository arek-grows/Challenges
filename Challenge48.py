import unittest
from typing import Optional, Tuple


################################################
###                                          ###
###   Implement the methods for this class   ###
###    to make the game work as intended     ###
###                                          ###
################################################

class Game:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.nr_turn = 1
        pass

    def get_scores(self) -> Tuple[int, int]:
        return self.p1_score, self.p2_score

    def is_game_over(self) -> bool:
        if self.p1_score == 21 or self.p2_score == 21:
            return True
        return False

    def turn(self, *dice: int):
        if self.nr_turn % 2 == 1:
            self.p1_score += sum(dice)
            if self.p1_score > 21:
                self.p1_score = 0
        else:
            self.p2_score += sum(dice)
            if self.p2_score > 21:
                self.p2_score = 0
        self.nr_turn += 1
        pass

    def winner(self) -> Optional[int]:
        if self.p1_score == 21:
            return 1
        elif self.p2_score == 21:
            return 2
        return None


#############################################
###                                       ###
###   Tests to make sure the game works   ###
###                                       ###
#############################################

class TestGame(unittest.TestCase):
    def game_1(self):
        game = Game()
        game.turn(1, 2, 3)  # Player 1 - 6
        game.turn(2, 3, 4)  # Player 2 - 9
        game.turn(1, 2, 3)  # Player 1 - 12
        game.turn(2, 3, 4)  # Player 2 - 18
        game.turn(1, 2, 3)  # Player 1 - 18
        game.turn(1, 1, 1)  # Player 2 - 21 - Game Over
        return game

    def test_1(self):
        game = self.game_1()
        self.assertTrue(game.is_game_over())

    def test_2(self):
        game = self.game_1()
        self.assertEqual(2, game.winner())

    def test_3(self):
        game = self.game_1()
        self.assertEqual((18, 21), game.get_scores())

    def game_2(self):
        game = Game()
        game.turn(1, 2, 3)  # Player 1 - 6
        game.turn(2, 3, 4)  # Player 2 - 9
        game.turn(1, 2, 3)  # Player 1 - 12
        game.turn(2, 3, 4)  # Player 2 - 18
        game.turn(1, 2, 3)  # Player 1 - 18
        game.turn(2, 3, 4)  # Player 2 - 0
        return game

    def test_4(self):
        game = self.game_2()
        self.assertFalse(game.is_game_over())

    def test_5(self):
        game = self.game_2()
        self.assertIsNone(game.winner())

    def test_6(self):
        game = self.game_2()
        self.assertEqual((18, 0), game.get_scores())

    def game_3(self):
        game = Game()
        game.turn(1, 2, 3, 4, 5)  # Player 1 - 15
        game.turn(2, 3, 4, 1, 1)  # Player 2 - 11
        game.turn(1, 2, 3, 4, 5)  # Player 1 - 0
        game.turn(2, 3, 4, 1, 1)  # Player 2 - 0
        game.turn(1, 2, 3, 1, 2)  # Player 1 - 9
        game.turn(2, 3, 4, 5, 6)  # Player 2 - 20
        game.turn(1, 2, 1, 1, 2)  # Player 1 - 16
        game.turn(2, 3, 4, 5, 6)  # Player 2 - 0
        game.turn(1, 1, 1, 1, 1)  # Player 1 - 21 - Game Over
        return game

    def test_7(self):
        game = self.game_3()
        self.assertTrue(game.is_game_over())

    def test_8(self):
        game = self.game_3()
        self.assertEqual(1, game.winner())

    def test_9(self):
        game = self.game_3()
        self.assertEqual((21, 0), game.get_scores())


if __name__ == "__main__":
    unittest.main()