from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0,y = 270)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"score: {self.score}, High Score: {self.highscore}",align="center",font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
        self.updatescore()
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"game over",align="center",font=("Arial", 30, "normal"))

    def incscore(self):
        self.score+=1
        self.updatescore()