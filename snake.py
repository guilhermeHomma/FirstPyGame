import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake_dir = [0,1]
snake_last_move = [0,1]
snake = [(200,200), (200-snake_dir[0]*10,200-snake_dir[1]*10), (200-snake_dir[0]*20,200-snake_dir[1]*20)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))



def collision(pos1, pos2):
    """
    return true if the objs are collinding
    """
    if (pos1[0] == pos2[0] and pos1[1] == pos2[1]):
        return True
    return False

def random_pos(): 
    """
    return random position
    """
    return (random.randint(0,59)*10, random.randint(0,59)*10)

apple_skin = pygame.Surface((10,10))
apple_skin.fill((255,0,0))
apple_pos = random_pos()
#dir = 
clock = pygame.time.Clock()

gameState = "DEFAULT"

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_w and snake_last_move != [0,1]:
                snake_dir = [0,-1]
            if event.key == K_s and snake_last_move != [0,-1]:
                snake_dir = [0,1]
            if event.key == K_a and snake_last_move != [1,0]:
                snake_dir = [-1,0]
            if event.key == K_d and snake_last_move != [-1,0]:
                snake_dir = [1,0]

    if collision(snake[0], apple_pos): 
        snake.append((0,0))
        apple_pos = random_pos()

    for i in range(len(snake)-1 , 0 ,-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    snake[0] = (snake[0][0]+snake_dir[0]*10, snake[0][1]+snake_dir[1]*10)
    snake_last_move = snake_dir

    for i in range(len(snake)-1 , 0 ,-1):
        if collision(snake[i], snake[0]):
            snake = [(200,200), (200-snake_dir[0]*10,200-snake_dir[1]*10), (200-snake_dir[0]*20,200-snake_dir[1]*20)]
            break

    screen.fill((0,0,0))
 
    screen.blit(apple_skin,apple_pos)

    for pos in snake:
        screen.blit(snake_skin,pos)

    

    pygame.display.update()       