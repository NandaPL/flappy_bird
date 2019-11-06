import pygame
import intro
import pipes
import sounds
import sprites

# variáveis para a movimentação do chão
ground_x = 0
shift = sprites.ground.get_width() - sprites.background.get_width()


def bg_loop(screen):
    global ground_x, shift
    # mostrando o chão e o background
    screen.blit(sprites.background, (0, 0))
    screen.blit(sprites.ground, (ground_x, 500))
    # movimentação do chão
    ground_x = -((-ground_x + 4) % shift)


# variáveis dos canos
i = 0
upper_y, lower_y = pipes.pipes_y()

# variável score
score = 0
font = pygame.font.SysFont('04B_19', 50)

pos_y = 230


def gameplay(screen):
    global i, score, upper_y, lower_y, pos_y

    # painel da pontuação
    score_hud = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_hud, (165, 20))

    # pássaro
    screen.blit(sprites.bird[0], (90, pos_y))

    # posicionamento aleatório dos canos (provisório)
    i += 1
    if i == 100:
        upper_y, lower_y = pipes.pipes_y()
        i = 0
    pipes.draw_pipes(screen, upper_y, lower_y)
