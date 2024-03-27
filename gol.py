
import numpy as np 
import tkinter as tk
class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.current_grid, self.next_grid = self.initialize_grids(rows, cols)

    def initialize_grids(self, rows, cols):
        current_grid = np.random.randint(2, size=(rows, cols))
        next_grid = np.random.randint(1, size=(rows, cols))
        return current_grid, next_grid


    def count_alive(grid, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0<= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] == 1:
                    neighbors += 1
        return neighbors

    def game_step(current_state, next_state):
        for x in range(len(current_state)):
            for y in range (len(current_state[0])):
                alive_neighbors = count_alive(current_state, x, y)
                if current_state[x][y] == 1 and alive_neighbors in (2,3):
                    next_state[x][y] = 1
                elif current_state[x][y] == 0 and alive_neighbors == 3:
                    next_state[x][y] = 1            
                else:
                    next_state[x][y] = 0
        return current_state, next_state