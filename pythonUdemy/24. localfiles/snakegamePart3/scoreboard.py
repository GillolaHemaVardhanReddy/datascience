from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt',mode="r") as file:
            content = file.read()
            self.highscore = content and int(content) or 0
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
            with open('data.txt',"w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.updatescore()
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!",align="center",font=("Arial", 30, "normal"))
        self.goto(0,-20)
        self.write(f"touch on screen to exit",align="center",font=("Arial", 20, "normal"))

    def incscore(self):
        self.score+=1
        self.updatescore()