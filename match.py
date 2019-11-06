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
upper_y, lower_y = pipes.pipes_y()

# variável score
score = 0
font = pygame.font.SysFont('04B_19', 50)

pos_y = 230

#espçamento de movimento
move_left = -4

x = 278

pipe_exist = False

def gameplay(screen):
    global spawn_xPipe, score, upper_y, lower_y, pos_y, x
    global upper_y2, lower_y2, pos_pipe2, pos_obj
    global pipe_exist
    
    spawn_xPipe = 278

    # painel da pontuação
    score_hud = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_hud, (165, 20))

    # pássaro
    screen.blit(sprites.bird[0], (90, pos_y))

    # posicionamento aleatório dos canos (provisório)
    if x < 0:
        #posição em y para mover
        pos_pipe = pipes.pipes_y()
        upper_y = pos_pipe[0]
        lower_y= pos_pipe[1]
        x = spawn_xPipe
    pipes.draw_pipes(screen, upper_y, lower_y, x)
    x += move_left

    if x == 100:
        pipe_exist = True
        #posição em y para mover
        pos_pipe2 = pipes.pipes_y()
        upper_y2 = pos_pipe2[0]
        lower_y2 = pos_pipe2[1]
        pos_obj = spawn_xPipe
    
    if pipe_exist:
        pipes.draw_pipes(screen, upper_y2, lower_y2, pos_obj)
        pos_obj += move_left



