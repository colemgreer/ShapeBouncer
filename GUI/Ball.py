import turtle
from turtle import *
import tkinter as tk



#forward(100)


#Function that creates a red ball
def createShape():
    window = tk.Tk();
    ball = turtle.Turtle();
    ball.shape("square");
    ball.color("red");
    window.mainloop();

createShape()