import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Shape Dropper")
root.geometry("800x760")

pane = tk.Frame(root)
pane.pack()

def draw_circle():
    canvas.delete("all")
    canvas.create_oval(33, 33, 100, 100, fill = "red")

def draw_square():
    canvas.delete("all")
    canvas.create_rectangle(33, 33, 100, 100, fill = "red")

def draw_triangle():
    canvas.delete("all")
    canvas.create_polygon(33, 33, 100, 33, 66, 100, fill = "red")

button = tk.Button(pane, text = "Drop Circle", command = draw_circle)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(pane, text = "Drop Square", command = draw_square)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(pane, text = "Drop Triangle", command = draw_triangle)
button.pack(side = "left", expand = True, fill = "both")

canvas = tk.Canvas(root, width = 400, height = 400)
canvas.pack()

root.mainloop()