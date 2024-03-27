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
    cell_size = 10
    for i in range (rows):
        for j in range (cols):
            color = "blue" if grid[i,j] == 1 else "white"
            canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill=color, outline="gray")

def run_and_canvas(field,iterations, delay = 100):
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
        

print(golly(50, 1000))