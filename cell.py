import numpy
import random
from grid import *

def get_neighbours(rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append(matrix[newRow][newCol])
    return result

#cell_state_t = f(neighbours_states_t-1)
class Cell:

    def __init__(self, i, j):
        self.rpos = i
        self.cpos = j
        self.value = random.choice([True, False])
        self.neighbours = get_neighbours(self.rval, self.cval)


    def count_neighbours(self):
        ncount = 0

        for neighbour in self.neighbours:
            if neighbour.value == True :
                ncount += 1

        return ncount

    # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    def next_state(self, neighbours_count):

        if self.value == True :
            #rule no.1
            if neighbours_count < 2:
                self.value = False
            #rule no.3            
            if neighbours_count > 3:
                self.value = False 
            #else rule no.2 will automatically be satisfied

        if self.value == False:
            if neighbours_count == 3:
                self.value = True

    def draw_cell(self):
        pass
