import tkinter as tk
from tkinter import ttk

x1 = 33
y1 = 33

x2 = 100
y2 = 100

root = tk.Tk()
root.title("Shape Dropper")
root.geometry("800x760")

top_pane = tk.Frame(root)
top_pane.pack()

middle_pane = tk.Frame(root)
middle_pane.pack()

bottom_pane = tk.Frame(root)
bottom_pane.pack()



gravity = 0.1
direction = 0

def draw_circle():

    global x1, x2, y1, y2
    top_canvas.delete("all")
    ball = top_canvas.create_oval(x1, y1, x2, y2, fill = "red")
    y1 += 0.1
    y2 += 0.1
    top_canvas.after(1, draw_circle)

def draw_square():
    top_canvas.delete("all")
    square = top_canvas.create_rectangle(33, 33, 100, 100, fill = "red")

def draw_triangle():
    top_canvas.delete("all")
    triangle = top_canvas.create_polygon(33, 33, 100, 33, 66, 100, fill = "red")

button = tk.Button(top_pane, text = "Drop Circle", command = draw_circle)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(top_pane, text = "Drop Square", command = draw_square)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(top_pane, text = "Drop Triangle", command = draw_triangle)
button.pack(side = "left", expand = True, fill = "both")


left_listbox = tk.Listbox(middle_pane, width=2, height=30)
left_listbox.pack(side = "left")

for z in range(30, -1, -1):
    left_listbox.insert(tk.END, str(z))


top_canvas = tk.Canvas(middle_pane, width = 740, height = 600, bg="skyblue")
top_canvas.pack(side="left", expand = True, fill = "both")

right_listbox = tk.Listbox(middle_pane, width=2, height=30)
right_listbox.pack(side = "right")

for z in range(30, -1, -1):
    right_listbox.insert(tk.END, str(z))

bottom_canvas = tk.Canvas(bottom_pane, width = 740, height = 100, bg="green")
bottom_canvas.pack(side="bottom", expand = True, fill = "both")

root.mainloop()