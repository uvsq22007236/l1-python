import tkinter as tk
import random

racine = tk.Tk()

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw(i, j, color):
    canvas.create_line(i, j, i + 1, j + 1, width = 1, fill = color)

def ecran_aleatoire():
    for i in range (256):
        for j in range (256):
            a = random.randint(0, 255)
            b =  random.randint(0, 255)
            c =  random.randint(0, 255)
            draw(i, j, get_color(a, b, c))

def degrade_gris():
    for i in range (256):
        for x in range(256):
            for j in range(256):
                draw(i, j, get_color(x, x, x))
            
def degrade_2D():
    r, g, b = 0, 0, 0
    for x in range(256):
        for y in range(256):
            r += x
            b += y
            draw(x, y, get_color(r, g, b))
            r, g, b = 0, 0, 0
            
        


canvas = tk.Canvas(racine, width = 255, height = 255, bg = "black")

Button1 = tk.Button(racine, text = "aléatoire", command = ecran_aleatoire)
Button2 = tk.Button(racine, text = "Dégradé gris", command = degrade_gris)
Button3 =tk.Button(racine, text = "Dégradé 2D", command = degrade_2D)

Button1.grid(row = 0, column = 0)
Button2.grid(row = 1, column = 0)
Button3.grid(row = 2, column = 0)
canvas.grid(row = 0, rowspan = 3, column = 1)

racine.mainloop()

