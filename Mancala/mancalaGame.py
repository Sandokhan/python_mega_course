class Mancala:
    def __init__(self):
        self.playerOne = True
        self.playing = True
        self.binAmount = [4] * 6 + [0] + [4] * 6 + [0]
        self.chooseBin = None
        self.giveawayPile = None
        self.lastRecipient = None

    def display_board(self):
        print('\nPLAYER 2\n' + ' '.join(
            ['{:>2}'.format(str(i)) for i in self.binAmount[12:6:-1]]) + '\n{:>2}{:>14}\n'.format(
            str(self.binAmount[13]), str(self.binAmount[6])) + ' '.join(
            ['{:>2}'.format(str(i)) for i in self.binAmount[0:6]]) + '\nPLAYER 1\n')

    def get_bin(self, userInput):
        return int(userInput) - 1 if self.playerOne else int(userInput) + 5

    def valid_bin(self, bin):
        return 0 <= bin <= 5 if self.playerOne else 7 <= bin <= 12

    def take_turn(self):
        if self.playerOne:
            message = "Player 1 turn..."
        else:
            message = "Player 2 turn..."

        print('\n', message, '\n')
        self.display_board()

        userInput = input("Choose a bin or enter 'q' to QUIT the game: ")

        if userInput == 'q':
            self.playing = False
        else:
            bin = self.get_bin(userInput)
            if not self.valid_bin(bin):
                msgCode = -2  # invalid entry
                print('Invalid input. Try again, Player', int(self.playerOne) + 1, '!')
            else:
                self.chooseBin = bin
                self.giveawayPile = self.binAmount[bin]
                self.binAmount[bin] = 0

                if self.giveawayPile <= 0:
                    print('You must choose a non-empty bin. Try again, Player', int(self.playerOne) + 1, '!')
                else:
                    self.lastRecipient = self.chooseBin + 1
                    while self.giveawayPile > 0:
                        if self.playerOne and self.lastRecipient == 13:
                            self.lastRecipient = 0
                        elif not self.playerOne and self.lastRecipient == 6:
                            self.lastRecipient = 7

                        self.binAmount[self.lastRecipient] += 1
                        self.giveawayPile -= 1
                        self.lastRecipient += 1

                    if self.lastRecipient == 7 and not self.playerOne:
                        print('Player 2 gets another turn!')
                    elif self.lastRecipient == 14 and self.playerOne:
                        print('Player 1 gets another turn!')
                    else:
                        self.playerOne = not self.playerOne


if __name__ == '__main__':
    g = Mancala()
    g.display_board()
    g.take_turn()
