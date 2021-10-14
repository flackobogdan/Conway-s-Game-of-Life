import pygame
import numpy as np
import random

class Grid:

    def __init__(self,  width, height, scale): #offset myb

        self.scale = scale
        self.cols = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.cols)
        self.grid_array = np.ndarray(shape=(self.size))

    def fill_the_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid_array[i][j] = random.randint(0,1)

    def count_cell_neighbours(self, i, j):
        total = 0

        for n in range(-1, 2):
            for m in range(-1, 2):
                i_edge = (i+n+self.rows) % self.rows
                j_edge = (j+m+self.cols) % self.cols
                total += self.grid_array[i_edge][j_edge]
    
        total -= self.grid_array[i][j]
        return total
    
    # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    def get_next_state(self):
        next_grid_state = np.ndarray(shape=(self.size))
        
        for i in range(self.rows):
            for j in range(self.cols):
                current_state = self.grid_array[i][j]
                neighbours_count = self.count_cell_neighbours(i,j)
                if current_state == 0 and neighbours_count == 3:
                    next_grid_state[i][j] = 1
                elif current_state == 1 and (neighbours_count < 2 or neighbours_count > 3):
                    next_grid_state[i][j] = 0
                else:
                    next_grid_state[i][j] = current_state
        
        self.grid_array = next_grid_state

    def draw_grid(self, on_color, off_color, surface):
        for i in range(self.rows):
            for j in range(self.cols):
                pos_i = i * self.scale
                pos_j = j * self.scale
                if self.grid_array[i][j] == 1:
                    pygame.draw.rect(surface, on_color, [pos_i, pos_j, self.scale, self.scale])
                else:
                    pygame.draw.rect(surface, off_color, [pos_i, pos_j, self.scale, self.scale])
