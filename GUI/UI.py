import tkinter as tk
from tkinter import ttk

def button_click():
    selected_item = dropdown.get()
    print("Selected item:", selected_item)

root = tk.Tk()
root.title("Shape Dropper")
root.geometry("800x760")

# Create a button
button = tk.Button(root, text="Drop Shape", command=button_click)

# Create a dropdown menu
dropdown = ttk.Combobox(root, values=["circle", "square", "triangle"])
dropdown.set("circle")  # Set the default option

dropdown.pack()
button.pack()

'''
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=1)

for z in range(40, -1, -1):
    listbox.insert(tk.END, z)
'''
canvas = tk.Canvas(root, width=400, height=400)

if button_click:
    canvas.delete("all")
    if dropdown.get() == "circle":
        canvas.create_oval(100, 100, 300, 300, fill="red")
    elif dropdown.get() == "square":
        canvas.create_rectangle(100, 100, 300, 300, fill="red")
    elif dropdown.get() == "triangle":
        canvas.create_polygon(100, 100, 300, 100, 200, 300, fill="red")

root.mainloop()