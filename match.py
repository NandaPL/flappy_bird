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
    global ground_obj
    # mostrando o chão e o background
    screen.blit(sprites.background, (0, 0))
    ground_obj = screen.blit(sprites.ground, (ground_x, 500))

    # movimentação do chão
    ground_x = -((-ground_x + 4) % shift)


# variáveis dos canos
i = 0
upper_y, lower_y = pipes.pipes_y()

# variável score
score = 0
font = pygame.font.SysFont('04B_19', 50)

bird_pos = incli = up = 0
down = 0
bird_y = 230
direc = list(range(-5, 1))
flapped = False
crash = False

#espçamento de movimento
move_left = -4

x = 278

pipe_exist = False

def gameplay(screen):
    global spawn_xPipe, score, upper_y, lower_y, pos_y, x
    global upper_y2, lower_y2, pos_pipe2, pos_obj
    global pipe_exist
    global crash, i 
    global bird_y, bird_pos, incli, flapped, up, down
    spawn_xPipe = 278

    # painel da pontuação
    score_hud = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_hud, (165, 20))

    # pássaro
    bird_incli = pygame.transform.rotate(sprites.bird[bird_pos], incli)
    bird_obj = screen.blit(bird_incli, (90, bird_y))
    if flapped:
        down = 0
        up += 1
        bird_y -= up
        incli = 25
        if up > 5:
            up = 0
            flapped = False
    else:
        down += 0.1
        bird_y += down
        if down > 5:
            down = 5
        incli -= 5
        if incli == 0:
            incli = 360
        if incli < 315 and incli > 45:
            incli = 315
    
    i += 1

    if i % 5 == 0 and crash == False:
        bird_pos += 1
    if bird_pos > 3:
        bird_pos = 0

    if (bird_obj.colliderect(ground_obj)):
        incli = 270
        bird_y = 472
        crash = True
        screen.blit(sprites.ground, (0, 500))
        #gameover(screen)


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



