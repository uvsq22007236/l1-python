import tkinter as tk 
import random

HEIGHT = 500
WIDTH = 500

racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH, relief="raised", borderwidth=25 )
canvas.grid(row=1, column=1, columnspan=3, rowspan =5)

objets=[]
couleur ="blue"
x1=random.randint(25, 400)
y1=random.randint(25, 400)
x2=random.randint(25, 400)
y2=random.randint(25, 400)
cercle=canvas.create_oval((x1, y1), (x2, y2), fill=couleur)
carre=canvas.create_rectangle((x1, y1), (x2, y2), fill=couleur)
ligne1=canvas.create_line((x1, y1), (x2, y2), fill=couleur, width=5)
ligne2=canvas.create_line((x1+100, y1), (x1, y2), fill=couleur, width=5)

def affiche_cerle():
    x1=random.randint(25, 400)
    y1=random.randint(25, 400)
    x2=random.randint(25, 400)
    y2=random.randint(25, 400)
    x2=100+x1
    y2=100+y1
    objets.append(canvas.create_oval((x1, y1), (x2, y2), fill=couleur))

def affiche_carre():
    x1=random.randint(25, 400)
    y1=random.randint(25, 400)
    x2=random.randint(25, 400)
    y2=random.randint(25, 400)
    x2=100+x1
    y2=100+y1
    objets.append(canvas.create_rectangle((x1, y1), (x2, y2), fill=couleur))

def affiche_croix():
    x1=random.randint(25, 400)
    y1=random.randint(25, 400)
    x2=random.randint(25, 400)
    y2=random.randint(25, 400)
    x2=100+x1
    y2=100+y1
    objets.append(canvas.create_line((x1, y1), (x2, y2), fill=couleur, width=5))
    objets.append(canvas.create_line((x1+100, y1), (x1, y2), fill=couleur, width=5))

def aleatoire_color():
    global couleur
    couleur = input("choisir une couleur")

def undo():
    global objets
    if canvas.type(objets[-1])=="line":
        canvas.delete(objets[-1])
        del objets[-1]
        canvas.delete(objets[-1])
        del objets[-1]
    else:
        canvas.delete(objets[-1])
        del objets[-1]


racine.title("Mon dessin")
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH, relief="raised", borderwidth=25 )
canvas.grid(row=1, column=1, columnspan=3, rowspan =5)
bouton1 = tk.Button(racine, text="choisir une couleur",font = ("Times", "15"), command=aleatoire_color)
bouton1.grid(row=0, column=1)
bouton2 = tk.Button(racine, text="cercle",font = ("Times", "15"), command=affiche_cerle)
bouton2.grid(row=1, column=0)
bouton3 = tk.Button(racine, text="Carre",font = ("Times", "15"), command=affiche_carre)
bouton3.grid(row=3, column=0)
bouton4 = tk.Button(racine, text="Croix",font = ("Times", "15"), command=affiche_croix)
bouton4.grid(row=5, column=0)
bouton5 = tk.Button(racine, text="Undo",font = ("Times", "15"),command=undo)
bouton5.grid(row=0, column=2)
racine.mainloop()
