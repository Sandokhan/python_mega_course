import pygame
from board import Board

def main():
    # Initialize Pygame
    pygame.init()

    # Set up screen
    screen = pygame.display.set_mode((620, 620))
    pygame.display.set_caption("Mancala")

    # Create board object
    board = Board()

    # Draw board
    draw_mancala_board(screen, board)

    # Update screen
    pygame.display.flip()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
