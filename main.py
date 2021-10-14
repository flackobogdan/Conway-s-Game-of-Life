import pygame
import random
import numpy as np
from pygame import display

#defining some colors:
black = (0,0,0)
white = (255,255,255)

if __name__=='__main__':
    
    width, height = 800, 600

    #setting a screen
    pygame.init()
    surface = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    fps = 30

    pause = False
    run = True

    

    while run:
        clock.tick(fps)
        surface.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.K_SPACE:
                pause = not pause
        


        pygame.display.update()

    pygame.quit()