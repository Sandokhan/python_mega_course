import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

#bat
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

#ball
ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (250, 250)
ball_speed = (3.0, 3.0)
ball_served = False
speedx, speedy = ball_speed
ball_rect.topleft = ball_start

bat_rect[1] = screen.get_height() - 100

#brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()
game_over = False
x,y = (0, 0)
while not game_over:

    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    # Adding Bricks
    for b in bricks:
        screen.blit(brick, b)

    # Adding Paddle
    screen.blit(bat, bat_rect)

    # Adding Ball
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()

    if pressed[K_LEFT]:
        x -= .5 * dt
    if pressed[K_RIGHT]:
        x += .5 * dt
    if pressed[K_SPACE]:
        ball_served = True

    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
            ball_rect[1] + ball_rect.height >= bat_rect[1] and speedy > 0:
        speedy *= -1
        # Increase dificulty
        speedx *= 1.01
        speedy *= 1.01
        continue

    delete_bricks = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width and by <= ball_rect[1] <= by + brick_rect.height :
            delete_bricks = b

            if ball_rect[0] <= bx + 2:
                speedx *= -1
            elif ball_rect[0] <= bx + brick_rect.width - 2:
                speedx *= -1
            if ball_rect[1] <= by + 2:
                speedy *= -1
            elif ball_rect[1] <= by + brick_rect.height - 2:
                speedy *= -1
            break

    if delete_bricks is not None:
        bricks.remove(delete_bricks)

    # Top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        speedy *= -1
    # Bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = ball_start
    # Left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        speedx *= -1
    # Right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        speedx *= -1

    bat_rect[0] = x
    if ball_served:
        ball_rect[0] += speedx
        ball_rect[1] += speedy
    pygame.display.update()
pygame.quit()