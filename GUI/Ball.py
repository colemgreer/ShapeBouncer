import turtle
from turtle import *
import tkinter as tk

window = tk.Tk()

#forward(100)


#Function that creates a red ball
def createShape(shapeName):
    ball = turtle.Turtle();
    ball.shape(shapeName);
    ball.color("red");

createShape("circle")
window.mainloop()