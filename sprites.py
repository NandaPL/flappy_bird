import pygame

pygame.init()
pygame.display.set_mode((338, 600))


# carregando as imagens
def sprite(image):
    load = pygame.image.load(image).convert_alpha()
    return load


btn_play = sprite('sprites/btn-play.png')

btn_rank = sprite('sprites/btn-rank.png')

logo = sprite('sprites/logo.png')

ground = sprite('sprites/ground.png')

background = sprite('sprites/bg.png')

bird = [sprite('sprites/bird-upflap.png'),
        sprite('sprites/bird-midflap.png'),
        sprite('sprites/bird-downflap.png'),
        sprite('sprites/bird-midflap.png')]
