import pygame
import sprites

# variáveis para a movimentação do pássaro na tela inicial
global move, pos, direc
pos = move = 0
direc = list(range(-8, 9))


def initiation(screen):
    global move, pos, direc, play_press, rank_press

    # mostrando o pássaro
    screen.blit(sprites.bird[pos], (153, 230+direc[move]))
    # mostrando a logo
    screen.blit(sprites.logo, (80, 120))
    # mostrando o botão play
    play_press = screen.blit(sprites.btn_play, (40, 410))
    # mostrando o botão rank
    rank_press = screen.blit(sprites.btn_rank, (190, 410))

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
