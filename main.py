import controls
import intro
import match
import pygame
import pipes

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((338, 600))
pygame.display.set_caption('Flappy Bird')
pygame.display.flip()

# variáveis para transições de tela
run = init = True
ready = game = False

# variaveis dos canos
i = 0
upper_y, lower_y = pipes.pipes_y()

while run:
    match.bg_loop(screen)

    # posicionamento aleatorio (provisorio)
    i += 1
    if i == 100:
        upper_y, lower_y = pipes.pipes_y()
        i = 0
    pipes.draw_pipes(screen, upper_y, lower_y)

    # tela inicial
    if init:
        intro.initial(screen)

    # tela intermediária (mensagem get ready)
    if ready:
        intro.get_ready(screen)

    # tela principal (partida)
    # if game:
        # função para iniciar o jogo

    # checagem de eventos
    for event in pygame.event.get():
        run = controls.close(event, run)
        init, ready = controls.play(event, init, intro.play_press, ready)
        ready, game = controls.instruction(event, ready, init, game)

    pygame.display.update()
    clock.tick(30)
