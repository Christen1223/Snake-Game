from random import randint
import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (138,43,226)
YELLOW = (255,255,0)
outline = 0

def redrawGameWindow():
    gameWindow.fill(BLACK)
    font = pygame.font.SysFont("Aldhabi",50)
    graphics = font.render("Score: " + str(score),1,WHITE)
    gameWindow.blit(graphics,(0,0))
    pygame.draw.rect(gameWindow,PURPLE,(appleX,appleY,radius,radius),outline)
    for i in snakeBody:
        pygame.draw.rect(gameWindow,YELLOW,(i[0],i[1],radius,radius),outline)
    pygame.display.update()

snakePos = [WIDTH/2,HEIGHT/2]
snakeBody = [list(snakePos)]
changeX = 0
changeY = 0
radius = 10
vert = True
hori = True

spawnApple = True

clock = pygame.time.Clock()
score = 0
inPlay = True
while inPlay:
    if spawnApple:
        appleX = randint(1,WIDTH/10 - 10) * 10
        appleY = randint(1,HEIGHT/10 - 10) * 10
        spawnApple = False

    redrawGameWindow()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and vert:
                changeX = 0
                changeY = -10
                vert = False
                hori = True
            elif event.key == pygame.K_DOWN and vert:
                changeX = 0
                changeY = 10
                vert = False
                hori = True
            elif event.key == pygame.K_LEFT and hori:
                changeX = -10
                changeY = 0
                vert = True
                hori = False
            elif event.key == pygame.K_RIGHT and hori:
                changeX = 10
                changeY = 0
                vert = True
                hori = False

    snakePos[0] += changeX
    snakePos[1] += changeY
    snakeBody.append(list(snakePos))

    if snakePos[0] < 0:
        inPlay = False
    elif snakePos[0] + radius > WIDTH:
        inPlay = False
    elif snakePos[1] < 0:
        inPlay = False
    elif snakePos[1] + radius > HEIGHT:
        inPlay = False

    for j in range(0,len(snakeBody) - 2):
        if pygame.Rect(snakeBody[j][0],snakeBody[j][1],radius,radius).colliderect(pygame.Rect(snakePos[0],snakePos[1],radius,radius)):
            inPlay = False

    if snakePos[0] == appleX and snakePos[1] == appleY:
        spawnApple = True
        score += 1
    else:
        snakeBody.pop(0)

    clock.tick(20)

pygame.quit()