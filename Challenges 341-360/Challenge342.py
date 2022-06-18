import unittest


def tic_tac_toe(board: list[list[str]]) -> str:
    for ii in range(3):
        if board[ii][ii] != "E":
            if board[0][ii] == board[1][ii] == board[2][ii]:
                return board[0][ii]
            elif board[ii][0] == board[ii][1] == board[ii][2]:
                return board[ii][0]
    if board[1][1] != "E":
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    return "Draw"  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]), "X"
        )

    def test_2(self):
        self.assertEqual(
            tic_tac_toe([["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]]), "O"
        )

    def test_3(self):
        self.assertEqual(
            tic_tac_toe([["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]), "Draw"
        )

    def test_4(self):
        self.assertEqual(
            tic_tac_toe([["X", "O", "O"], ["X", "O", "O"], ["X", "X", "X"]]), "X"
        )

    def test_5(self):
        self.assertEqual(
            tic_tac_toe([["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]), "Draw"
        )

    def test_6(self):
        self.assertEqual(
            tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["E", "E", "X"]]), "X"
        )

    def test_7(self):
        self.assertEqual(
            tic_tac_toe([["X", "O", "E"], ["X", "O", "E"], ["E", "O", "X"]]), "O"
        )


if __name__ == "__main__":
    unittest.main()