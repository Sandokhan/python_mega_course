"""
This class is responsible for staring all the information about the curren state od a chess_yt game. It will also be
responsible for determining the valid move at the current state. It will also keep a move log.
"""
import numpy as np


class GameState:
    def __init__(self):
        # Board 8x8 2d list, each element of the list has 2 characters,
        # The first letter represents the color of piece 'b' or 'w'
        # The second letter represents the type, 'K', 'Q', 'R', 'B', 'N', 'p'
        #  '--' represents empty space.
        self.board_array = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.board = np.array(self.board_array)
        self.whiteToMove = True
        self.moveLog = []
