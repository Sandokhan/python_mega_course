from copy import deepcopy

START_STATE = ([4] * 6 + [0]) * 2


class PocketName:
    num_pockets = 14

    p0_mancala = 6
    p1_mancala = 13

    p0_pockets = list(range(6))
    p1_pockets = list(range(12, 6, -1))


class GameState:
    def __init__(self, init_state=START_STATE, player_turn=0, stealing=True):
        self.state = init_state
        self.player_turn = player_turn
        self.stealing = stealing
        self.winner = None

    def show(self):
        print()
        print("Player {}'s turn:".format(self.player_turn))
        print("      5   4   3   2   1   0")
        print("[{:2}]({:2})({:2})({:2})({:2})({:2})({:2})[  ]".format(*self.state[-1:6:-1]))
        print("[  ]({:2})({:2})({:2})({:2})({:2})({:2})[{:2}]".format(*self.state[:7]))
        print("      0   1   2   3   4   5")

    def show_winning_message(self):
        print(f"Player {self.winner} Won!")

    def is_terminal(self):
        if self.winner is not None:
            return True
        return False

    def children(self):
        for move in self.possible_moves():
            new_state = self.make_move(move)
            yield move, new_state

    def possible_moves(self):
        if self.player_turn == 0:
            for i in PocketName.p0_pockets:
                if self.state[i] != 0:
                    yield i
        else:
            for i in PocketName.p1_pockets:
                if self.state[i] != 0:
                    yield i

    def make_move(self, move):
        # assumes that the move is valid
        player0_turn = self.player_turn == 0

        new_state = deepcopy(self.state)
        hand = new_state[move]
        new_state[move] = 0

        while hand > 0:
            move = (move + 1) % PocketName.num_pockets
            if (player0_turn and move == PocketName.p1_mancala) or (not player0_turn and move == PocketName.p0_mancala):
                # skip opponent's mancala
                continue
            hand -= 1
            new_state[move] += 1

        if self.stealing:
            if (player0_turn and move in PocketName.p0_pockets) or (not player0_turn and move in PocketName.p1_pockets):
                if new_state[move] == 1:
                    # steal marbles from opposite pocket if your pocket was empty
                    opposite_move = 12 - move
                    hand = new_state[move] + new_state[opposite_move]
                    new_state[move], new_state[opposite_move] = 0, 0

                    if player0_turn:
                        new_state[PocketName.p0_mancala] += hand
                    else:
                        new_state[PocketName.p1_mancala] += hand

        if (player0_turn and move == PocketName.p0_mancala) or (not player0_turn and move == PocketName.p1_mancala):
            # play again if last peice is put in your own mancala
            next_player = self.player_turn
        else:
            next_player = 1 - self.player_turn

        # check for winner
        game_done = sum(new_state[:6]) == 0 or sum(new_state[7:13]) == 0
        winner = None
        if game_done:
            if sum(new_state[:6]) == 0:
                new_state[PocketName.p1_mancala] += sum(new_state[7:13])
                for i in PocketName.p1_pockets:
                    new_state[i] = 0
            elif sum(new_state[7:13]) == 0:
                new_state[PocketName.p0_mancala] += sum(new_state[:6])
                for i in PocketName.p0_pockets:
                    new_state[i] = 0
            winner = 0 if new_state[PocketName.p0_mancala] > new_state[PocketName.p1_mancala] else 1

        new_game_state = GameState(new_state, next_player, self.stealing)
        new_game_state.winner = winner
        return new_game_state


class Player:
    pass


class HumanPlayer(Player):
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, state):
        move = None
        print()
        while move not in state.possible_moves():
            move = int(input("Enter move [0,5]: "))

            if self.player_id == 1:
                move = move + 7

        new_state = state.make_move(move)
        return new_state


default_ai_dificulty = 6


def player_player_game():
    player_0 = HumanPlayer(0)
    player_1 = HumanPlayer(1)
    play_game(player_0, player_1)


#
# def player_ai_game(ai_difficulty):
#     player_0 = HumanPlayer(0)
#     player_1 = AIPlayer(1, ai_difficulty)
#     play_game(player_0, player_1)
#
# def ai_player_game(ai_difficulty):
#     player_0 = AIPlayer(0, ai_difficulty)
#     player_1 = HumanPlayer(1)
#     play_game(player_0, player_1)
#
# def ai_ai_game(ai0_difficulty, ai1_difficulty):
#     player_0 = AIPlayer(0, ai0_difficulty)
#     player_1 = AIPlayer(1, ai1_difficulty)
#     play_game(player_0, player_1)


def play_game(player_0, player_1, stealing_mode=True):
    game_state = GameState(stealing=stealing_mode)

    while not game_state.is_terminal():
        game_state.show()
        if game_state.player_turn == 0:
            game_state = player_0.move(game_state)
        else:
            game_state = player_1.move(game_state)
    game_state.show()
    game_state.show_winning_message()


if __name__ == "__main__":
    player_player_game()
    # ai_ai_game(default_ai_dificulty, default_ai_dificulty)
# if __name__ == "__main__":
#     game_state = GameState()
#     print(game_state.state)
#     game_state.show()
