import pygame

pygame.init()
pygame.display.set_mode((338, 600))


# carregando as imagens
def sprite(image):
    load = pygame.image.load(image).convert_alpha()
    return load


background = sprite('sprites/bg.png')

ground = sprite('sprites/ground.png')

logo = sprite('sprites/logo.png')

btn_play = sprite('sprites/btn-play.png')

btn_rank = sprite('sprites/btn-rank.png')

btn_rate = sprite('sprites/btn-rate.png')

get_ready = sprite('sprites/get-ready.png')

tap_instru = sprite('sprites/tap.png')

game_over = sprite('sprites/game-over.png')

final_score = sprite('sprites/final-score.png')

bird = [sprite('sprites/bird-upflap.png'),
        sprite('sprites/bird-midflap.png'),
        sprite('sprites/bird-downflap.png'),
        sprite('sprites/bird-midflap.png')]

pipe_down = sprite('sprites/pipe-down.png')

pipe_up = sprite('sprites/pipe-upq.png')
