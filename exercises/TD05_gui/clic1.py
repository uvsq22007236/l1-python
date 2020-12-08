import tkinter as tk

def draw_pixel(event):
    canvas.create_line((event.x, event.y), (event.x + 1, event.y), fill= "red")

racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500,  height= 500, bg = "black")

canvas.bind("<Button-1>", draw_pixel)
canvas.grid()

racine.mainloop()