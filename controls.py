import pygame
from pygame import event
from sounds import swooshing, wing, play_sound


# evento para fechar o jogo
def close(event, run):
    if event.type == pygame.QUIT:
        run = False
    return run


# evento para checar se o botão play foi pressionado
def play(event, init, play_press, ready):
    if (event.type == pygame.MOUSEBUTTONDOWN and
       event.button == 1 and
       play_press.collidepoint(event.pos) and
       init):
        init = False
        ready = True
        play_sound(swooshing)
    return init, ready


def ready_to_play(event, ready, init, game):
    if (ready and event.type == pygame.KEYDOWN and
       event.key == pygame.K_SPACE):
        ready = False
        game = True
    return ready, game


def bird_player(event, game, flapped):
    if (game and event.type == pygame.KEYDOWN and
       event.key == pygame.K_SPACE):
        flapped = True
        play_sound(wing)
    return flapped
