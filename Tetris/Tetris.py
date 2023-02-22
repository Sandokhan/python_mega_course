import pygame

pygame.init()

# Set up the display
display_width = 500
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Tetris")

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        screen.fill((0, 0, 0))
        pygame.display.update()
pygame.quit()