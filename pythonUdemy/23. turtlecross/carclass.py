from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
pencil = Turtle()
pencil.hideturtle()

class Car:
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE
    
    def createcar(self):
        if rd.randint(1,6)==1:
            newcar = Turtle("square")
            newcar.shapesize(stretch_len=2,stretch_wid=1)
            newcar.penup()
            newcar.color(rd.choice(COLORS))
            y = rd.randint(-250,250)
            newcar.goto(300,y)
            self.cars.append(newcar)
    def writestart(self,time):
        if time==41:
            pencil.write("Start",align="center",font=("Courier", 34, "normal"))
        if time==46:
            pencil.clear()
        
    def write(self,text):
        pencil.write(text,align="center",font=("Courier", 34, "normal"))
    def move(self):
        for car in self.cars:
            car.backward(self.carspeed)

    def levelup(self):
        self.carspeed += MOVE_INCREMENT