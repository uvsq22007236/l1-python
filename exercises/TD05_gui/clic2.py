import tkinter as tk

def draw_circle(event):
    if event.x < 250:
        color = "blue"
    else:
        color = "red"
    canvas.create_oval((event.x-50, event.y-50), (event.x + 50, event.y+50), fill= color)

racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500,  height= 500, bg = "black")
canvas.create_line((250,0), (250,500), fill= "white")
canvas.bind("<Button-1>", draw_circle)
canvas.grid()

racine.mainloop()