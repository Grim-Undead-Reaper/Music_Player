import pygame
from pygame.locals import *
import sys, os
from Constantes import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

clock = pygame.time.Clock()

while run:

    clock.tick(60)

    screen.fill(COLORS['white'])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    
    pygame.display.flip()