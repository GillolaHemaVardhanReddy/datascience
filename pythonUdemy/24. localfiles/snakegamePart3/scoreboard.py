from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0,y = 270)
        self.updatescore()

    def updatescore(self):
        self.write(f"score: {self.score}",align="center",font=("Arial", 20, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"game over",align="center",font=("Arial", 30, "normal"))

    def incscore(self):
        self.score+=1
        self.clear()
        self.updatescore()