import pygame
import copy

# Define game constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PIT_WIDTH = 50
PIT_HEIGHT = 150
PIT_PADDING = 10
STONE_RADIUS = 20
PIT_COLOR = (128, 64, 0)
STONE_COLOR = (255, 255, 255)
PLAYER_1 = 0
PLAYER_2 = 1

# Define game state representation
class GameState:
    def __init__(self, board=None, player=PLAYER_1, score=None):
        if board is None:
            self.board = [[4]*6, [4]*6, [0, 0]]
        else:
            self.board = board
        self.player = player
        if score is None:
            self.score = [0, 0]
        else:
            self.score = score
    
    def get_legal_moves(self):
        moves = []
        for i in range(6):
            if self.board[self.player][i] > 0:
                moves.append(i)
        return moves
    
    def make_move(self, move):
        board_copy = copy.deepcopy(self.board)
        stones = board_copy[self.player][move]
        board_copy[self.player][move] = 0
        i = move
        while stones > 0:
            i = (i + 1) % 14
            if i != 6:
                board_copy[self.player][i] += 1
                stones -= 1
        if i == 6 and self.player == PLAYER_1:
            self.score[self.player] += 1
        elif i == 13 and self.player == PLAYER_2:
            self.score[self.player] += 1
        elif board_copy[self.player][i] == 1 and i < 6 and board_copy[self.opponent()][5-i] > 0:
            self.score[self.player] += board_copy[self.opponent()][5-i] + 1
            board_copy[self.player][i] = 0
            board_copy[self.opponent()][5-i] = 0
        return GameState(board=board_copy, player=self.opponent(), score=self.score)
    
    def opponent(self):
        return PLAYER_2 if self.player == PLAYER_1 else PLAYER_1

# Implement Minimax algorithm with alpha-beta pruning
def minimax(state, depth, alpha, beta, max_player):
    if depth == 0 or state.score[0] >= 24 or state.score[1] >= 24:
        return state.score[max_player] - state.score[1-max_player]
    if max_player:
        best_value = float('-inf')
        for move in state.get_legal_moves():
            child_state = state.make_move(move)
            value = minimax(child_state, depth-1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('inf')
        for move in state.get_legal_moves():
            child_state = state.make_move(move)
            value = minimax(child_state, depth-1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value

# Initialize Pygame
pygame.init()
screen = pygame.display