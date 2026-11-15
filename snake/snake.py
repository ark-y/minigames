import tkinter 
import random 

rows = 25
columns = 25
tile_size = 25

window_width = tile_size * columns
window_height = tile_size * rows

#game window 
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = window_width, height = window_height)
canvas.pack()
window.update()

window.mainloop()