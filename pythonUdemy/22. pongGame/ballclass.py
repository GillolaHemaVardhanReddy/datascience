from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto((0,0))
        self.x = 10
        self.y = 10
        self.speedy = 0.1
    
    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto((x,y))

    def bouncey(self):
        self.y *=-1
    
    def bouncex(self):
        self.x *=-1
    
    def detectcollision(self,paddle1=None,paddle2=None):
        if self.ycor() > 280 or self.ycor() < -280 :
            self.bouncey()
        if self.distance(paddle1) < 50 and self.xcor() > 330 or self.distance(paddle2) < 50 and self.xcor() < -320 :
            self.speedy *= 0.9
            self.bouncex()

    def resetposition(self):
        self.speedy = 0.1
        self.goto(0,0)
        self.bouncex()
        