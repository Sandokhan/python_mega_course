import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((700, 700), 0, 32)
sprite1 = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (32, 32))

spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()

pygame.display.set_caption("Hello Keyboard")

x, y = (0,0)
game_over = False
clock = pygame.time.Clock()
while not game_over:

    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()

    if pressed[K_UP]:
        y-= .5 * dt
    if pressed[K_DOWN]:
        y+= .5 * dt
    if pressed[K_LEFT]:
        x-= .5 * dt
    if pressed[K_RIGHT]:
        x+= .5 * dt
    if pressed[K_SPACE]:
        x, y = (0, 0)

    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth

    if x < 0:
        x = 0

    if y > (screen.get_height() - spriteHeight):
        y = screen.get_height() - spriteHeight

    if y < 0:
        y = 0

    screen.fill((0,0,0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
