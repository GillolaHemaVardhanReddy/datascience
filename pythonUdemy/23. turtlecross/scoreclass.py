from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.color("blue")
        self.goto(-280,260)
        self.writelevel()
    
    def updatelevel(self):
        self.clear()
        self.level += 1
        self.writelevel()
    
    def writelevel(self):
        self.write(f"Level {self.level}",align="left",font=FONT) 