import pygame
import controls
import intro
import match

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((338, 600))
pygame.display.set_caption('Flappy Bird')
pygame.display.flip()

# variáveis para transições de tela
run = init = True
ready = game = False

while run:
    match.bg_loop(screen)

    # tela inicial
    if init:
        intro.initial(screen)

    # tela intermediária (mensagem get ready)
    if ready:
        intro.get_ready(screen)

    # tela principal (partida)
    if game:
        match.gameplay(screen)

    # checagem de eventos
    for event in pygame.event.get():
        run = controls.close(event, run)
        init, ready = controls.play(event, init, intro.play_press, ready)
        ready, game = controls.ready_to_play(event, ready, init, game)
        match.flapped = controls.bird_player(event, game, match.flapped)

    pygame.display.update()
    clock.tick(30)
