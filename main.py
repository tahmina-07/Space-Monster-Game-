import pygame
import random
#intialize the pygame
pygame.init()

#create a screen for our game
screen = pygame.display.set_mode((800, 600))

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
enemyIcon = pygame.image.load('octopus.png')
eX = random.randint(0, 800)
eY = random.randint(50, 150)
eX_change = 0.3
eY_change = 40

def player(x, y):
    screen.blit(playerIcon, (x, y)) #draw the img on the screen

def enemy(x, y):
    screen.blit(enemyIcon, (x, y)) #draw the img on the screen

#main loop 
#set a flag and we use while so the screen will last longer 
running = True 
while running:
    #add backround color to the main window
    screen.fill((176, 38, 255))
    
    #loop over all the events 
    for event in pygame.event.get():
        #if a quit button is pressed we will set the flag to false
        if event.type == pygame.QUIT:
            running = False
        #checking the buttons for movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -0.3
            if event.key == pygame.K_RIGHT:
                pX_change = 0.3
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
    
    eX += eX_change
    #set boundries for enemy 
    if eX <= 0:
        eX_change = 0.3
        eY += eY_change
    elif eX >= 736: # imgPix = 64 | 800 - 64 = 736
        eX_change = -0.3
        eY += eY_change
                
    player(pX, pY)
    enemy(eX, eY)
    pygame.display.update()





