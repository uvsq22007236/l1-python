import tkinter as tk 

cpt = 0
def alterne(event):
    global cpt
    if cpt % 2 == 0:
        color = "white"
    else:
        color = "black"
    cpt += 1 
    canvas.itemconfigure(rectangle, fill = color)
    if cpt > 9:
        racine.destroy()

racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500,  height= 500, bg = "black")
rectangle = canvas.create_rectangle((100, 100), (400, 400), outline = "white", fill= "black")
canvas.bind("<Button-1>", alterne)
canvas.grid()
racine.mainloop()