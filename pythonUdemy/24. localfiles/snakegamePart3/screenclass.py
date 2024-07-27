from turtle import Screen
import time

w = 600
h = 600
screencolor = "black"
title = "Snake Game"

class ScreenCtrl:
    """
        1. this class is used to control screen according to our uses
        2. starts to listen to screen
    """
    def __init__(self):
        """
            this constructor creates screen for snake game of 
            width 600 and height 600
            bg color
            title
        """
        self.screen = Screen()
        self.quit = 0
        self.screen.setup(width=w,height=h)
        self.screen.bgcolor(screencolor)
        self.screen.title(title)
        self.screen.tracer(0)
        self.screen.listen() 

    def updatechange(self):
        self.screen.update()
        time.sleep(0.1)

    def exit(self):
        self.quit = 1

    def exitcondition(self):
        self.screen.onkeypress(self.exit,"Escape")
    
    def exittouch(self):
        self.screen.exitonclick()