import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) # création du widget root=premier interphase graphique, donc toujours en premier!!

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100 #500
y = CANVAS_HEIGHT / 2 #200
canvas.create_line(x0, y, x1, y) #(100,200)(500,200)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
# Fin de votre code
canvas.grid() #.pack()
root.mainloop()


import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) # création du widget root=premier interphase graphique, donc toujours en premier!!

# Début de votre code
y1 = 100
y2 = CANVAS_HEIGHT - 100 #300
x = CANVAS_WIDTH // 2 #300
canvas.create_line((x, y1), (x, y2))

canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50) #(250, 150), (350, 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50) #(250, 350), (350, 250)
canvas.create_oval(x - 50, (y1 + y2) // 2 + 50, x + 50, (y1 + y2) // 2 - 50)

# Fin de votre code
canvas.grid()
root.mainloop()
