# Challenge 227 - Connect Four
#
# Take a look at wiki description of Connect Four game: https://en.wikipedia.org/wiki/Connect_Four
#
# The grid is 6 rows by 7 columns, the columns being named A to G.
#
# You will receive a list of strings showing the order of the pieces which were dropped into the columns:
#
# pieces_position_list = ["A_Red",
#                         "B_Yellow",
#                         "A_Red",
#                         "B_Yellow",
#                         "A_Red",
#                         "B_Yellow",
#                         "G_Red",
#                         "B_Yellow"]
#
# The list may contain up to 42 moves and shows the order the players are playing.
#
# The first player who connects four items of the same color is the winner.
#
# You should return "Yellow", "Red" or "Draw" accordingly.


from __future__ import annotations
import unittest


def search_win(plays: list[str], color: str) -> bool:
    count = 0
    for play in plays:
        if play == color:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def who_is_winner(plays: list[str]) -> str:
    game_board = [[''] * 7, [''] * 7, [''] * 7, [''] * 7, [''] * 7, [''] * 7]
    positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for play in plays:
        position_y = positions.index(play.split('_')[0])
        color = play.split('_')[1]
        # color = color[0]
        # search game board x position from bottom
        for x in range(5, -1, -1):
            # if blank, attach color
            if game_board[x][position_y] == '':
                game_board[x][position_y] = color
                # search for a win

                # scan horizontal list
                if search_win(game_board[x], color):
                    return color

                # create vertical list
                vertical_list = []
                for i in range(0, 6):
                    vertical_list.append(game_board[i][position_y])
                # scan vertical list
                if search_win(vertical_list, color):
                    return color

                # create forward diagonal list (/)
                f_diagonal_list = []
                current_x = x
                current_y = position_y
                # - append the left, down most position
                # to go down x, add. to go left y, subtract
                while current_x < 5 and current_y > 0:
                    current_x += 1
                    current_y -= 1
                f_diagonal_list.append(game_board[current_x][current_y])
                # - append all up+right positions, stop at x == 0, y == 6
                while current_x > 0 and current_y < 6:
                    current_x -= 1
                    current_y += 1
                    f_diagonal_list.append(game_board[current_x][current_y])
                # scan f diagonal list
                if len(f_diagonal_list) >= 4:
                    if search_win(f_diagonal_list, color):
                        return color

                # create back diagonal list (\)
                b_diagonal_list = []
                current_x = x
                current_y = position_y
                # - append the right, down most position
                # to go down x, add. to go right y, add
                # if current_x == 5 or current_y == 6:
                #     f_diagonal_list.append(game_board[current_x][current_y])
                # else: 
                while current_x < 5 and current_y < 6:
                    current_x += 1
                    current_y += 1
                b_diagonal_list.append(game_board[current_x][current_y])
                # - append all up+left positions, stop at x == 0, y == 0
                while current_x > 0 and current_y > 0:
                    current_x -= 1
                    current_y -= 1
                    b_diagonal_list.append(game_board[current_x][current_y])
                # scan b diagonal list
                if len(b_diagonal_list) >= 4:
                    if search_win(b_diagonal_list, color):
                        return color

                # break, since we already attached the color into position
                break
    return "Draw"  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(who_is_winner([
            "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
            "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
            "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
        ]), "Yellow")

    def test_2(self):
        self.assertEqual(who_is_winner([
            "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
            "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
            "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
            "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
            "E_Yellow", "E_Red"
        ]), "Yellow")

    def test_3(self):
        self.assertEqual(who_is_winner([
            "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
            "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
            "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
            "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
            "B_Yellow", "B_Red"
        ]), "Red")

    def test_4(self):
        self.assertEqual(who_is_winner([
            "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
            "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
        ]), "Red")

    def test_5(self):
        self.assertEqual(who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
        ]), "Yellow")

    def test_6(self):
        self.assertEqual(who_is_winner([
            "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
        ]), "Draw");


if __name__ == "__main__":
    unittest.main()
