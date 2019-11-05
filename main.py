import sprites
import start
import pygame
from pygame import event

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((338, 600))
pygame.display.set_caption('Flappy Bird')
pygame.display.flip()

# variáveis para a movimentação da base
ground_x = 0
shift = sprites.ground.get_width() - sprites.background.get_width()

running = intro = True
while running:

    # mostrando os sprites do fundo
    screen.blit(sprites.background, (0, 0))
    screen.blit(sprites.ground, (ground_x, 500))

    # movimentação da base
    ground_x = -((-ground_x + 4) % shift)

    if intro:
        start.initiation(screen)

    for event in pygame.event.get():
        # evento para fechar o jogo
        if event.type == pygame.QUIT:
            running = False
        # evento para checar se o botão play foi pressionado
        if (event.type == pygame.MOUSEBUTTONDOWN and
           event.button == 1 and
           start.play_press.collidepoint(event.pos)):
            intro = False

    pygame.display.update()
    clock.tick(30)
