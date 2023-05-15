#Drawing a cicle usuing turtle in python

import turtle
import random


t = turtle.Turtle()

turtle.setup(400, 400)
turtle.bgcolor("white")

def circle():
    t.pencolor("black")
    t.fillcolor("yellow")
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(10, 50)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    
circle()
turtle.done()
