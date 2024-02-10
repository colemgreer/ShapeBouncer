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
dropdown = ttk.Combobox(root, values=["Circle", "Square", "Triangle"])
dropdown.set("Circle")  # Set the default option

dropdown.pack()
button.pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=1)

for z in range(40, -1, -1):
    listbox.insert(tk.END, z)


root.mainloop()