import random as rd
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def square(pencil):
    """this function draws a square"""
    for i in range(4):
        pencil.forward(100)
        pencil.left(90)
    return

def dotLine(pencil,n):
    """this function is use to draw a dotted line with n no.of intervals"""
    for i in range(1,n+1):
        pencil.forward(10)
        if(i&1):
            pencil.penup()
        else:
            pencil.pendown()
    return

def multiGrams(pencil):
    """this function draws multiple shapes tending outwards from triangle to sepagon"""
    for i in range(3,8):
        pencil.color(rd.choice(colours))
        for j in range(i):
            pencil.forward(50)
            angle = 360//i 
            pencil.left(angle)
    return

def randomWalk(pencil):
    directions = [0,90,180,270]
    pencil.pensize(15)
    for i in range(rd.randint(1,100)):
        pencil.color(rd.choice(colours))
        pencil.forward(50)
        pencil.setheading(rd.choice(directions))
    return

def spiral(pencil):
    for i in range(50):
        pencil.speed(0)
        pencil.color(rd.choice(colours))
        pencil.circle(100)
        pencil.setheading(pencil.heading() + 10)
    return


def moveToStart(pencil):
    pencil.setheading(90)
    pencil.forward(50)
    pencil.setheading(180)
    pencil.forward(500)
    pencil.setheading(0)