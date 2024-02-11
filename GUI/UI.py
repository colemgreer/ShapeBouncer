import tkinter as tk
from tkinter import ttk

def button_click():
    selected_item = dropdown.get()
    print("Selected item:", selected_item)

root = tk.Tk()
root.title("Shape Dropper")
root.geometry("800x760")

'''
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=1)

for z in range(40, -1, -1):
    listbox.insert(tk.END, z)
'''

def draw_circle():
    canvas.delete("all")
    canvas.create_oval(100, 100, 300, 300, fill="red")

def draw_square():
    canvas.delete("all")
    canvas.create_rectangle(100, 100, 300, 300, fill="red")

def draw_triangle():
    canvas.delete("all")
    canvas.create_polygon(100, 100, 300, 100, 200, 300, fill="red")

button = tk.Button(root, text="Drop Circle", command=draw_circle)
button.pack()

button = tk.Button(root, text="Drop Square", command=draw_square)
button.pack()

button = tk.Button(root, text="Drop Triangle", command=draw_triangle)
button.pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()