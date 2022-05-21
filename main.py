import pygame
#intialize the pygame
pygame.init()

#create a screen for our game
screen = pygame.display.set_mode((800, 600))

#set a flag and we use while so the screen will last longer 
running = True 
while running:
    #loop over all the events 
    for event in pygame.event.get():
        #if a quit button is pressed we will set the flag to false
        if event.type == pygame.QUIT:
            running = False



