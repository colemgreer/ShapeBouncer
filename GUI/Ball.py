import turtle
from turtle import *
import tkinter as tk

window = tk.Tk()

#forward(100)


#Function that creates a red ball
def createBall():
    ball = turtle.Turtle();
    ball.shape("circle");
    ball.color("red");

createBall()
window.mainloop()