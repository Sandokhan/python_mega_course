import pygame
from pygame import Vector2
from pygame.transform import rotozoom
from random import randint


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
        self.velocity = Vector2(randint(-3, 3), randint(-3, 3))
        self.image = pygame.image.load('images/asteroid1.png')

    def update(self):
        self.position += self.velocity
        if self.position.x < out_of_bound[0] or self.position.x > out_of_bound[2]:
            self.velocity.x *= -1
        if self.position.y < out_of_bound[1] or self.position.x > out_of_bound[3]:
            self.velocity.y *= -1


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
asteroids = [Asteroid((randint(0, screen.get_width()), randint(0, screen.get_height()))) for i in range(10)]

out_of_bound = [-150, -150, 950, 950]
clock = pygame.time.Clock()

while not game_over:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        screen.blit(background, (0, 0))

        ship.update()
        ship.draw(screen)

        for a in asteroids:
            a.update()
            a.draw(screen)

        pygame.display.update()
pygame.quit()
