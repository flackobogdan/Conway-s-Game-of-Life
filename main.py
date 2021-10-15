import pygame
import random
import numpy as np
from pygame import display
import grid_and_cells

#defining some colors:
black = (0,0,0)
white = (255,255,255)

if __name__=='__main__':
    
    width, height = 800, 600

    #setting a screen
    pygame.init()
    surface = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    fps = 15

    pause = False
    run = True

    scaler = 10
    
    grid = grid_and_cells.Grid(width, height, scaler)
    grid.fill_the_grid()
    grid.draw_grid(white,black,surface)
    # pygame.display.update()

    while run:
        clock.tick(fps)

        key_state = pygame.key.get_pressed()
        
        if key_state[pygame.K_ESCAPE]:    
            run = False
        if key_state[pygame.K_SPACE]:
            pause = not pause

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        grid.get_next_state(pause)
        grid.draw_grid(white,black,surface)

        pygame.display.update()

    pygame.quit()