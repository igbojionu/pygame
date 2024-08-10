import pygame

#initialize pygame
pygame.init()

#create a game window
screen = pygame.display.set_mode((800,600))

# Set Window Title
pygame.display.set_caption("My first game")

#Main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Quit Pygame
pygame.quit()