from turtle import Turtle,Screen
from challenges import square,dotLine,multiGrams,randomWalk,spiral

pencil = Turtle()
screen = Screen()

pencil.shape("turtle")
pencil.color("black")

# to make turtle to run forward we use .forware(n) n-> distance to travel in
# pencil.forward(100)

# to change direction of the turtle we use right(x),left(x) x-> degrees wrt its relative position
# pencil.right(90)

# challenge 1
# square(pencil)

# challenge 2
# dotLine(pencil,50)

# challenge 3
# multiGrams(pencil)

# challenge 4
# randomWalk(pencil)

# challeng 5
spiral(pencil)

screen.exitonclick()