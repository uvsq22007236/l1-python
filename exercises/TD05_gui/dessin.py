import tkinter as tk
import random as rd 

ma_couleur = "blue"

def choisir():
    global ma_couleur
    ma_couleur = input("Choisir une couleur")

    
def cercle():
    x = rd.randint(0, 501)
    y = rd. randint(0,501)
    canvas.create_oval((x,y), (x+ 100, y + 100), fill= ma_couleur)

def carre():
    x = rd.randint(0,501)
    y  = rd.randint(0,501)
    canvas.create_rectangle((x,y), (x+100,y+100), fill= ma_couleur)

def croix():
    x = rd.randint(0, 501)
    y = rd. randint(0,501)
    canvas.create_line((x,y), (x+ 100, y + 100), fill= ma_couleur)
    canvas.create_line((x+100,y), (x, y+ 100), fill= ma_couleur)

racine = tk.Tk()
racine.title("Mon Dessin")
#creation widget
bouton_couleur = tk.Button(racine, text="choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=choisir)

bouton_cercle = tk.Button(racine, text="cercle", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=cercle)
bouton_carre = tk.Button(racine, text="carre", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=carre)
bouton_croix = tk.Button(racine, text="croix", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=croix)

canvas = tk.Canvas(racine, width = 500,  height= 500, bg = "black", bd=10, relief="raised")

#placement des widgets
bouton_couleur.grid ( row=0, column= 1)
bouton_cercle.grid (row=1, column=0)
bouton_carre.grid (row=2, column=0)
bouton_croix.grid (row= 3, column=0)

canvas.grid(row = 1, column = 1, rowspan= 3)
racine.mainloop()

