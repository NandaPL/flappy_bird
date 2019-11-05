import sprites
import intro
import pygame


# variáveis para a movimentação da base
ground_x = 0
shift = sprites.ground.get_width() - sprites.background.get_width()


def bg_loop(screen):
    global ground_x, shift
    # mostrando os sprites do fundo
    screen.blit(sprites.background, (0, 0))
    screen.blit(sprites.ground, (ground_x, 500))
    # movimentação da base
    ground_x = -((-ground_x + 4) % shift)
