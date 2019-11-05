import pygame
import sprites

# variáveis para a movimentação do pássaro na tela inicial
pos = move = 0
direc = list(range(-8, 9))


def initial(screen):
    global move, pos, direc, play_press, rank_press

    # mostrando pássaro, logo, botões play e rank
    screen.blit(sprites.logo, (80, 120))
    play_press = screen.blit(sprites.btn_play, (40, 410))
    rank_press = screen.blit(sprites.btn_rank, (190, 410))
    screen.blit(sprites.bird[pos], (153, 230+direc[move]))

    # movimentação do pássaro
    move += 1
    # mudança da posição das asas
    if move % 5 == 0:
        pos += 1
    if pos > 3:
        pos = 0
    # subidas e descidas
    if move > 16:
        move = 0
        direc.reverse()


def get_ready(screen):
    global move, pos, direc
    # mostrando pássaro, get ready e instrução
    screen.blit(sprites.get_ready, (80, 150))
    screen.blit(sprites.tap_instru, (115, 230))
    screen.blit(sprites.bird[pos], (90, 230+direc[move]))
    # movimentação do pássaro
    move += 1
    # mudança da posição das asas
    if move % 5 == 0:
        pos += 1
    if pos > 3:
        pos = 0
    # subidas e descidas
    if move > 16:
        move = 0
        direc.reverse()
