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

snake_body = [] #multiple snake tiles

velocity_x, velocity_y = 0, 0

game_end = False

def change_direction(e):
    #e = event 
    print(e.keysym)

    global velocity_x, velocity_y

    if(game_end):
        return

    if (e.keysym == "Up" and velocity_y != 1):
        velocity_x, velocity_y = 0, -1
    elif (e.keysym == "Down" and velocity_y != -1):
        velocity_x, velocity_y = 0, 1
    elif (e.keysym == "Left" and velocity_x != 1):
        velocity_x, velocity_y = -1, 0
    elif (e.keysym == "Right" and velocity_x != -1):
        velocity_x, velocity_y = 1, 0

def move():
    global snake, food, snake_body, game_end

    if(game_end):
            return

    if(snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height):
            game_end = True
            return

    for tile in snake_body:
        if(snake.x == tile.x and snake.y == tile.y):
            game_end = True
            return
    
    #snake eats food 
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))

        food.x = random.randint(0, columns - 1) * tile_size
        food.y = random.randint(0, rows - 1) * tile_size

    #update the snake body 
    for i in range(len(snake_body) - 1, -1, -1):
        
        tile = snake_body[i - 1]

        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else: 
            prev_tile = snake_body[i]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocity_x * tile_size
    snake.y += velocity_y * tile_size

def draw():
    global snake
    move()

    canvas.delete("all") #clear the canvas

    #draw the food 
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill = "blue")

    #draw the snake 
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill = "white")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + tile_size, tile.y + tile_size, fill = "white")
    
    window.after(100, draw) #100ms (0.1 second, 10 frames per second)

draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()