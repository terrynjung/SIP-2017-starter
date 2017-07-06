from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

sides = input("How many sides:")
intsides = int(sides)

t.pensize(5)

if intsides > 0 and intsides <= 3:
    t.pencolor("pink")
if intsides > 3 and intsides <= 6:
    t.pencolor("blue")
if intsides > 6 and intsides <= 10:
    t.pencolor("coral")
if intsides > 10:
    t.pencolor("cyan")

t.pendown()

for draw in range(intsides):
    t.forward(50)
    t.right(360/intsides)

# Close window on click.
exitonclick()
