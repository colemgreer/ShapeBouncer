import tkinter as tk
from tkinter import ttk

def button_click():
    selected_item = dropdown.get()
    print("Selected item:", selected_item)

root = tk.Tk()
root.title("Shape Dropper")
root.geometry("300x200")

# Create a button
button = tk.Button(root, text="Drop Shape", command=button_click)

# Create a dropdown menu
dropdown = ttk.Combobox(root, values=["Circle", "Square", "Triangle"])
dropdown.pack()
button.pack()

root.mainloop()