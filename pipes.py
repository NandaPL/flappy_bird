import pygame
import sprites
import random

# canos mais baixos
# screen.blit(sprites.pipe_down, (278, 0))
# screen.blit(sprites.pipe_up, (278, 470))

# intermediario
# screen.blit(sprites.pipe_down, (278, -100))
# screen.blit(sprites.pipe_up, (278, 370))

# canos mais altos
# screen.blit(sprites.pipe_down, (278, -280))
# screen.blit(sprites.pipe_up, (278, 190))


def pipes_y():
    pipe_gap = 470
    upper_y = random.randint(-280, 0)
    lower_y = upper_y + pipe_gap
    return upper_y, lower_y


def draw_pipes(screen, upper_y, lower_y):
    pipe_gap = 470
    x = 278  # ajustar quando houver o movimento
    screen.blit(sprites.pipe_down, (x, upper_y))
    screen.blit(sprites.pipe_up, (x, lower_y))
