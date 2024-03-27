
import numpy as np 
import tkinter as tk

class Rules:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Generate the initial state with the specified probabilities
        self.current_state = np.random.choice([0, 1], size=(rows, cols), p=[0.95, 0.05])
        self.next_state = np.random.choice([0, 1], size=(rows, cols), p=[0.95, 0.05])

    def count_alive(self, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x+i < self.rows and 0 <= y+j < self.cols and self.current_state[x+i][y+j] == 1:
                    neighbors += 1
        return neighbors

    def game_step(self):
        for x in range(self.rows):
            for y in range (self.cols):
                self.alive_neighbors = self.count_alive(x, y)
                if self.current_state[x][y] == 1 and self.alive_neighbors in (2,3):
                    self.next_state[x][y] = 1
                elif self.current_state[x][y] == 0 and self.alive_neighbors == 3:
                    self.next_state[x][y] = 1            
                else:
                    self.next_state[x][y] = 0
        self.current_state, self.next_state = self.next_state, self.current_state  

    def run_iterations(self, iterations):
        iteration_count = [0]

        def step():
            if iteration_count[0] < iterations:
                next_state, current_state = game_step(current_state, next_state)
                iteration_count[0] += 1
                field.after(delay, step)
            else:
                print("Simulation complete.")

        step()
