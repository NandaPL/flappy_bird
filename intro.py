import pygame
import sprites

# variáveis para a movimentação do pássaro na tela inicial
pos = move = 0
direc = list(range(-8, 9))


def bird_fly(screen, x, y):
    global move, pos, direc
    screen.blit(sprites.bird[pos], (x, y+direc[move]))
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


def initial(screen):
    global play_press, rank_press, rate_press

    # mostrando pássaro, logo, botões play e rank
    screen.blit(sprites.logo, (80, 120))
    play_press = screen.blit(sprites.btn_play, (40, 410))
    rank_press = screen.blit(sprites.btn_rank, (190, 410))
    rate_press = screen.blit(sprites.btn_rate, (137, 310))
    bird_fly(screen, 153, 230)


def get_ready(screen):
    # mostrando pássaro, get ready e instrução
    screen.blit(sprites.get_ready, (80, 150))
    screen.blit(sprites.tap_instru, (115, 230))
    bird_fly(screen, 90, 230)
