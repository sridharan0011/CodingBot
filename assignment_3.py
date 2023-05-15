#drawing bot in python
import turtle

def draw_shape(shapes):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    if shapes == "circle":
        turtle.circle(50)
    elif shapes == "square":
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif shapes == "triangle":
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif shapes == "rectangle":
        for i in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
    elif shapes == "pattern":
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
    else:
        print("Invalid shape.")


shapes = ""
while shapes != "q":
    shapes = input("choose any of the shape (circle, rectangle, pattern, square, triangle), or q to quit: ")
    if shapes != "q":
        draw_shape(shapes)

turtle.done()
