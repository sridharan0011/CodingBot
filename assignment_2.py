#Drawing a pattern using python

import turtle


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pattern")
t = turtle.Turtle()
t.speed(0)
t.color("black")


for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)


turtle.exitonclick()
