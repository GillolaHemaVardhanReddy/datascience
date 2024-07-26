from turtle import Screen
import time

w = 600
h = 600
screencolor = "white"
title = "TURTLE CROSS Game"

class ScreenCtrl:
    """
        1. this class is used to control screen according to our uses
        2. starts to listen to screen
    """
    def __init__(self):
        """
            this constructor creates screen for pong game of 
            width 800 and height 600
            bg color
            title
        """
        self.screen = Screen()
        self.screen.setup(width=w,height=h)
        self.screen.bgcolor(screencolor)
        self.screen.title(title)
        self.screen.tracer(0)
        self.screen.listen() 

    def updatechange(self,speed):
        self.screen.update()
        time.sleep(speed)

    def keyboardctrl(self,func):
        self.screen.onkeypress(func.up,"Up")

    def exitcondition(self):
        self.screen.exitonclick()