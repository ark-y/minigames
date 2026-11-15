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

window.mainloop()