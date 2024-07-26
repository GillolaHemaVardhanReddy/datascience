from turtle import Screen
import time

w = 800
h = 600
screencolor = "black"
title = "PONG Game"

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

    def keyboardctrl(self,func1,func2):
        self.screen.onkeypress(func1.up,"Up")
        self.screen.onkeypress(func1.down,"Down")
        self.screen.onkeypress(func2.up,"w")
        self.screen.onkeypress(func2.down,"s")

    def exitcondition(self):
        self.screen.exitonclick()