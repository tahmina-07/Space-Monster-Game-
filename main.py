import pygame
#intialize the pygame
pygame.init()

#create a screen for our game
screen = pygame.display.set_mode((800, 600))

#creating the caption and logo of the game 
pygame.display.set_caption("Space Monsters")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


# Adding playes 
playerIcon = pygame.image.load('alien.png')

#main loop 
#set a flag and we use while so the screen will last longer 
running = True 
while running:
    #loop over all the events 
    for event in pygame.event.get():
        #if a quit button is pressed we will set the flag to false
        if event.type == pygame.QUIT:
            running = False
    #add backround color to the main window
    screen.fill((176, 38, 255))
    pygame.display.update()





