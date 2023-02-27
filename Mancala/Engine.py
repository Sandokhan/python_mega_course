from random import *


class Player:
    """ Setting type of Players. """
    HUMAN = 0
    RANDOM = 1
    MINMAX = 2
    ABPRUNE = 3

    def __init__(self, playerNum, playerType, ply=0):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        # self.ply = ply

    def __repr__(self):
        """ Return a Representation of the Player"""
        return str(self.num)

    def chooseMove(self, board):
        """ Returns the next move that this player wants to make """
        if self.type == self.HUMAN:
            move = input("Please enter your move:")
            while not board.legalMove(self, move):
                print(move, "is not valid")
                move = input("Please enter your move")
            return move
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            print("chose move", move)
            return move
        elif self.type == self.MINIMAX:
            val, move = self.minimaxMove(board, self.ply)
            print("chose move", move, " with value", val)
            return move
        elif self.type == self.ABPRUNE:
            val, move = self.alphaBetaMove(board, self.ply)
            print("chose move", move, " with value", val)
            return move
        elif self.type == self.CUSTOM:

            val, move = self.alphaBetaMove(board, 14)
            print("chose move", move, " with value", val)
            return move
        else:
            print("Unknown player type")
            return -1


if __name__ == '__main__':
    p = Player(1, Player.HUMAN)
    print(p)
