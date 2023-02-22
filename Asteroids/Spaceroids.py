import pygame
from pygame import Vector2
from pygame import rotozoom


class Ship:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/ship.png')
        self.forward = Vector2((0, -1))

    def update(self):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_UP]:
            self.position += self.forward
        if is_key_pressed[pygame.K_LEFT]:
            self.forward = self.forward.rotate(-1)
        if is_key_pressed[pygame.K_RIGHT]:
            self.forward = self.forward.rotate(1)

    def draw(self, screen):
        angle = self.forward.angle_to(Vector2(0, -1))
        rotated_surface = rotozoom(self.image, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size // 2
        screen.blit(rotated_surface, blit_position)

class Asteroid:

    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/asteroid1.png')

    def update(self):
        pass

    def draw(self, position):
        screen.blit(self.image, self.position)


pygame.init()

# Set up the display
display_width = 800
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Roids")
background = pygame.image.load('images/space.png')

game_over = False
ship = Ship((100, 700))
astro1 = Asteroid((235, 345))
clock = pygame.time.Clock()

while not game_over:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        screen.blit(background, (0, 0))

        ship.update()
        ship.draw(screen)

        astro1.update()
        astro1.draw(screen)

        pygame.display.update()
pygame.quit()
