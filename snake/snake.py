import tkinter 
import random 

rows = 25
columns = 25
tile_size = 25

window_width = tile_size * columns
window_height = tile_size * rows

class Tile: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window 
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = window_width, height = window_height, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#centering the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#formatting window --> "(width)x(height)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialise game 
snake = Tile(5 * tile_size, 5 * tile_size) #the snake's head
food = Tile(10 * tile_size, 10 * tile_size)

velocity_x, velocity_y = 0, 0

def change_direction(e):
    #e = event 
    print(e.keysym)

    global velocity_x, velocity_y

    if (e.keysym == "Up" or e.keysym == "w"):
        velocity_x, velocity_y = 0, -1
    elif (e.keysym == "Down" or e.keysym == "s"):
        velocity_x, velocity_y = 0, 1
    elif (e.keysym == "Left" or e.keysym == "a"):
        velocity_x, velocity_y = -1, 0
    elif (e.keysym == "Right" or e.keysym == "d"):
        velocity_x, velocity_y = 1, 0

def move():
    global snake

    snake.x += velocity_x * tile_size
    snake.y += velocity_y * tile_size

def draw():
    global snake
    move()

    #draw the snake 
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill = "white")

    #draw the food 
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill = "blue")

    window.after(100, draw) #100ms (0.1 second, 10 frames per second)

draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()