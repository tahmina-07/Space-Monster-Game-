
import math
from pygame import mixer
import pygame
import random


#intialize the pygame
pygame.init()

#create a screen for our game
screen = pygame.display.set_mode((800, 600))

#backround
backround = pygame.image.load('backround.png')
# backround sound 
mixer.music.load('forest-lullaby-110624.mp3')
mixer.music.play(-1)

#creating the caption and logo of the game 
pygame.display.set_caption("Space Monsters")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


# Adding playes 
playerIcon = pygame.image.load('ufo.png')
pX = 370
pY = 480
pX_change = 0
pY_change = 0

# Adding Enemy
enemyIcon = []
eX = []
eY = []
eX_change = []
eY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyIcon.append(pygame.image.load('octopus.png'))
    eX.append(random.randint(0, 735))
    eY.append(random.randint(50, 150))
    eX_change.append(4)
    eY_change.append(40)


# Adding bullet
bulletIcon = pygame.image.load('love.png')
bX = 0
bY = 480
bX_change = 0
bY_change = 10
bState = "ready"

#score
score = 0
font = pygame.font.Font('Like Eat.ttf', 32)
tx = 10
ty = 10

#game over text
text = pygame.font.Font('Like Eat.ttf', 64)



def show_score(x, y):
    Score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(Score, (x, y))

def game_over():
    text_game = text.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(text_game, (200, 250))

def player(x, y):
    screen.blit(playerIcon, (x, y)) #draw the img on the screen

def enemy(x, y, i):
    screen.blit(enemyIcon[i], (x, y)) #draw the img on the screen

def fire_bullet(x, y):
    global bState
    bState = "fire"
    screen.blit(bulletIcon, (x + 16, y + 10))

def is_collision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY,2)))
    if distance < 27:
        return True
    else:
        return False

#main loop 
#set a flag and we use while so the screen will last longer 
running = True 
while running:
    #add backround color to the main window
    screen.fill((176, 38, 255))
    
    #backround img
    screen.blit(backround, (0, 0))
    #loop over all the events 
    for event in pygame.event.get():
        #if a quit button is pressed we will set the flag to false
        if event.type == pygame.QUIT:
            running = False
        #checking the buttons for movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -5
            if event.key == pygame.K_RIGHT:
                pX_change = 5
            if event.key == pygame.K_SPACE:
                sound = mixer.Sound('mixkit-game-whip-shot-1512.wav')
                sound.play()
                if bState is "ready":
                    bX = pX 
                    fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                 pX_change = 0
    pX += pX_change
    #setting the boundries 
    #set boundries for player
    if pX <= 0:
        pX = 0
    elif pX >= 736: # imgPix = 64 | 800 - 64 = 736
        pX = 736
    
    
    #set boundries for enemy
    for i in range(num_of_enemy):

        #game over
        if eY[i] > 400:
            for j in range(num_of_enemy):
                eY[j] = 2000
            game_over()
            break
        eX[i] += eX_change[i] 
        if eX[i] <= 0:  
            eX_change[i] = 4
            eY[i] += eY_change[i]
        elif eX[i] >= 736: # imgPix = 64 | 800 - 64 = 736
            eX_change[i] = -4
            eY[i] += eY_change[i]
        #collision
        collision = is_collision(eX[i], eY[i], bX, bY)
        if collision:
            sound_exp = mixer.Sound('mixkit-digital-cartoon-falling-405.wav')
            sound.play()
            bY = 480
            bState = "ready"
            score += 1
            eX[i] = random.randint(0, 735)
            eY[i] = random.randint(50, 150)
        enemy(eX[i], eY[i], i)

    #bullet movment
    if bY <= 0:
        bY = 480 
        bState = "ready"
    if bState is "fire":
        fire_bullet(bX, bY)
        bY -= bY_change  

    
    
    player(pX, pY)
    show_score(tx, ty)
    pygame.display.update()





