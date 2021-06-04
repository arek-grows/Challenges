# Challenge 212 - Maze Escape
#
# Given a maze as a two-dimensional list and a list of directions, create a function that follows the directions through the maze.
#
#     If you can reach the endpoint before all your moves have gone, return "Finish".
#     If you hit any walls or go outside the maze border, return "Dead".
#     If you find yourself still in the maze after using all the moves, return "Lost".
#
# The maze list will look like this:
#
# maze = [
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
# [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
# [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
# [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
# [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
# [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
# [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
# [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
# ]
#
# 0 = Safe place to walk
# 1 = Wall
# 2 = Start Point
# 3 = Finish Point
# N = North, E = East, W = West and S = South
# Examples
#
# exit_maze(maze, ["N", "E", "E"]) ➞ "Dead"
# # Hitting the wall should return "Dead".
# exit_maze(maze, ["N", "N", "N", "E"]) ➞ "Lost"
# # Couldn't reach the finish point.
# exit_maze(maze, ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"]) ➞ "Finish"


from __future__ import annotations
import unittest

N = [-1, 0]
E = [0, 1]
W = [0, -1]
S = [1, 0]


def exit_maze(maze, directions) -> str:
    # start is at maze[9][8]
    current = 2
    y = 9
    x = 8
    for direction in directions:
        if direction == 'N':
            y += N[0]
            x += N[1]
        elif direction == 'E':
            y += E[0]
            x += E[1]
        elif direction == 'W':
            y += W[0]
            x += W[1]
        elif direction == 'S':
            y += S[0]
            x += S[1]
        if y >= 10 or x >= 10:
            return "Dead"
        current = maze[y][x]
        if current == 1:
            return "Dead"
        elif current == 3:
            return "Finish"
    return "Lost"  # Put your code here!!!


class Tests(unittest.TestCase):
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 2, 1],
    ]

    def test_1(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "N", "N", "W", "W", "W", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"],
            ),
            "Finish",
        )

    def test_2(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "N", "N", "N", "N", "N", "N", "N", "W", "W", "W", "S", "W", "W", "N"],
            ),
            "Lost",
        )

    def test_3(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N","N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"],
            ),
            "Dead",
        )

    def test_4(self):
        self.assertEquals(exit_maze(self.maze, ["N","W", "W", "W", "W"]), "Dead")

    def test_5(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "N", "N", "N", "N", "N", "N", "N", "N", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            ),
            "Lost",
        )

    def test_6(self):
        self.assertEquals(exit_maze(self.maze, ["N","E",  "E"]), "Dead")

    def test_7(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N", "S", "S"],
            ),
            "Finish",
        )

    def test_8(self):
        self.assertEquals(exit_maze(self.maze, ["N","W", "W", "W", "N", "N"]), "Lost")

    def test_9(self):
        self.assertEquals(exit_maze(self.maze, ["N","N", "N", "E"]), "Lost")

    def test_10(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "N", "N", "W", "W", "W", "N", "N", "W", "W", "S", "S", "S", "S", "S", "S"],
            ),
            "Dead",
        )

    def test_11(self):
        self.assertEquals(
            exit_maze(
                self.maze,
                ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"],
            ),
            "Finish",
        )


if __name__ == "__main__":
    unittest.main()
