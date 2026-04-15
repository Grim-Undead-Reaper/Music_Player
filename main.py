import pygame
from pygame.locals import *
import sys, os
from Constantes import *
from tkinter import filedialog

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
playing = False
paused = False

clock = pygame.time.Clock()

while run:

    clock.tick(60)

    screen.fill(COLORS['white'])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                filepath = filedialog.askopenfilename(title="Choice you file", initialdir="/", filetypes=(("music files", ".mp3"),("music files",".wav")))
                try:
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(str(filepath))
                except:
                    pass
            
            if event.key == K_p:
                if playing == False:
                    if paused == True:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.play()
                    playing = True
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    playing = False
    
    pygame.display.flip()