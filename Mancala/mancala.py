import numpy as np


class Mancala:
    def __init__(self):
        self.binAmount = np.array([0 if i in (6, 13) else 4 for i in range(14)])
        self.playing = True
        self.playerOne = True
        self.msgCode = 0
        self.giveawayPile = -1
        self.lastRecipient = -1
        self.chooseBin = -1

    def display_board(self):
        binAmount = [str(x).rjust(2, ' ') for x in self.binAmount]
        print('\n')
        if not self.playerOne:
            print("        a    b    c    d    e    f")
        print('+----+----+----+----+----+----+----+----+')
        print(
            f'|    | {binAmount[12]} | {binAmount[11]} | {binAmount[10]} | {binAmount[9]} | {binAmount[8]} | {binAmount[7]} |    |')
        print(f'+ {binAmount[13]} +----+----+----+----+----+----+ {binAmount[6]} +')
        print(
            f'|    | {binAmount[0]} | {binAmount[1]} | {binAmount[2]} | {binAmount[3]} | {binAmount[4]} | {binAmount[5]} |    |')
        print('+----+----+----+----+----+----+----+----+')
        if self.playerOne:
            print("        f   e    d    c    b    a")
        print("")

    def get_user_input(self):
        userInput = input("Choose a bin or enter 'q' to QUIT the game: ")
        if userInput == 'q':
            self.playing = False
            self.chooseBin = 0
        elif userInput in ['a', 'b', 'c', 'd', 'e', 'f'] and self.playerOne:
            self.chooseBin = 5 - ord(userInput) + ord('a')
        elif userInput in ['a', 'b', 'c', 'd', 'e', 'f'] and not self.playerOne:
            self.chooseBin = ord(userInput) - ord('a') + 7
        else:
            self.chooseBin = -1
            self.msgCode = -2

    def check_invalid_input(self):
        if int(self.chooseBin) >= 0:
            self.giveawayPile = self.binAmount[self.chooseBin]
            self.binAmount[self.chooseBin] = 0
            if int(self.giveawayPile) <= 0:
                self.msgCode = -1
        recipient = self.chooseBin + 1
        while int(self.giveawayPile) > 0:
            if self.playerOne and int(recipient) == 13:
                recipient = 0
            if not self.playerOne and int(recipient) == 6:
                recipient = 7

            self.binAmount[recipient] = int(self.binAmount[recipient]) + 1
            self.giveawayPile = int(self.giveawayPile) - 1

            if int(self.giveawayPile) == 0:
                self.lastRecipient = recipient
            else:
                recipient = int(recipient) + 1
                if int(recipient) > 13:
                    recipient = 0

    def start_game(self):
        while self.playing:
            self.display_board()
            self.get_user_input()


x = Mancala()
x.display_board()
