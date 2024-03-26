
import numpy as np 
import tkinter as tk

def initialize_grids(rows, cols):
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

def create_window(size, iterations):
    root = tk.Tk()
    field = tk.Canvas(root, width=600,height=600)
    field.pack()
    next_button = tk.Button(root, text="100 Iterations", command=lambda : run_and_canvas(field, iterations, size))
    next_button.pack()
    init_button = tk.Button(root, text="New Initialization", command=lambda : initialize_and_draw_grid(field, size))
    init_button.pack()
    tk.mainloop()

def initialize_and_draw_grid(field, size):
    global current_grid, next_grid
    current_grid, next_grid = initialize_grids(size, size)
    draw_grid(field, current_grid)

def draw_grid(canvas, grid):
    canvas.delete("all")
    rows, cols = grid.shape
    cell_size = 5
    for i in range (rows):
        for j in range (cols):
            color = "blue" if grid[i,j] == 1 else "white"
            canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill=color, outline="gray")

def run_and_canvas(field,iterations, delay = 10):
    global current_grid, next_grid
    iteration_count = [0]

    def step():
        if iteration_count[0] < iterations:
            global current_grid, next_grid
            next_grid, current_grid = game_step(current_grid, next_grid)
            draw_grid(field, current_grid)
            iteration_count[0] += 1
            field.after(delay, step)
        else:
            print("Simulation complete.")

    step()

def golly(size, iterations):
    global current_grid, next_grid
    current_grid, next_grid = initialize_grids(size, size)
    create_window(size, iterations)
        

print(golly(75, 1000))