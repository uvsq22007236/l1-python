import tkinter as tk 

cpt = 0
cercles = []
def dixcercles(event):
    global cpt, cercles
    if cpt < 8:
        c = canvas.create_oval((event.x-50, event.y-50), (event.x + 50, event.y+50), fill= "red")
        cercles.append(c)
    elif cpt == 8:
        for c in cercles:
            canvas.itemconfigure(c, fill = "yellow")
    else:
        for c in cercles:
            canvas.delete(c)
        cercles = []
    cpt +=1

racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500,  height= 500, bg = "black")
canvas.bind("<Button-1>", dixcercles)
canvas.grid()
racine.mainloop()