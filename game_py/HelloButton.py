import pygame

pygame.init()

screen = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption("Hello Button")

text_coulor = (255, 255, 255)
button_coulor = (0, 0, 170)
button_over_coulor = (255, 50, 50)

button_width = 100
button_height = 50

button_rect = [screen.get_width()/2 - button_width/2,
               screen.get_height()/2 - button_height/2,
               button_width, button_height]

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(screen, button_coulor, button_rect)
    pygame.display.update()

pygame.quit()