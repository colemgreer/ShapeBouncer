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
velocity = 0
xvelocity = 1

def draw_circle():

    global x1, x2, y1, y2, z1, gravity, velocity, xvelocity
    top_canvas.delete("all")
    ball = top_canvas.create_oval(x1, y1, x2, y2, fill = "red")
    
    y1 -= velocity
    y2 -= velocity

    x1 += xvelocity
    x2 += xvelocity

    velocity -= gravity

    if(y2 >= 600):
        velocity *= -1
        if(velocity > 0.5):
            velocity -= 0.60
        else:
            velocity = 0
    
    if(x2 >= 740):
        xvelocity *= -1
    elif(x1 <= 0):
        xvelocity *= -1

    if(velocity == 0):
        top_canvas.after_cancel(top_canvas)
    else:    
        top_canvas.after(10, draw_circle)
        
    

def draw_square():
    global x1, x2, y1, y2, z1, gravity, velocity, xvelocity
    top_canvas.delete("all")
    square = top_canvas.create_rectangle(x1, y1, x2, y2, fill = "red")
    
    y1 -= velocity
    y2 -= velocity

    x1 += xvelocity
    x2 += xvelocity

    velocity -= gravity

    if(y2 >= 600):
        velocity *= -1
        if(velocity > 0.5):
            velocity -= 0.60
        else:
            velocity = 0
    
    if(x2 >= 740):
        xvelocity *= -1
    elif(x1 <= 0):
        xvelocity *= -1

    if(velocity == 0):
        top_canvas.after_cancel(top_canvas)
    else:    
        top_canvas.after(10, draw_square)

def reset():
    global x1, x2, y1, y2, z1
    top_canvas.delete("all")
    top_canvas.after_cancel(top_canvas)
   
    x1 = y1 = 33
    x2 = y2 = 100
    z1 = 66



button = tk.Button(top_pane, text = "Drop Circle", command = draw_circle)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(top_pane, text = "Drop Square", command = draw_square)
button.pack(side = "left", expand = True, fill = "both")

button = tk.Button(top_pane, text = "Reset", command = reset)
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