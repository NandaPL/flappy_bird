import pygame
from pygame.locals import QUIT

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
pygame.display.flip()


def sprite(image):
    load = pygame.image.load(image).convert_alpha()
    return load


logo = sprite('sprites/logo.png')

ground = sprite('sprites/ground.png')

background = sprite('sprites/background.png')

bird = [sprite('sprites/bird-upflap.png'),
        sprite('sprites/bird-midflap.png'),
        sprite('sprites/bird-downflap.png'),
        sprite('sprites/bird-midflap.png')]

pos = move = 0
direc = list(range(-8, 9))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(background, (0, -100))
    screen.blit(bird[pos], (180, 250+direc[move]))
    screen.blit(logo, (60, 100))
    screen.blit(ground, (0, 520))

    move += 1
    if move % 5 == 0:
        pos += 1
    if pos > 3:
        pos = 0

    if move > 16:
        move = 0
        direc.reverse()

    pygame.display.update()
    clock.tick(30)
