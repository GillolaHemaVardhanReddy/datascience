from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(pos)
    
    def up(self):
        y = self.ycor() + 20 
        self.goto(self.xcor(),y)
    
    def down(self):
        y = self.ycor() - 20 
        self.goto(self.xcor(),y)
    
    
