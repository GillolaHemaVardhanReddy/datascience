from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.gotostart()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def gotostart(self):
        self.goto(STARTING_POSITION)
    
    def collision(self,cars):
        for car in cars:
            if self.distance(car) < 20 :
                return True
        return False

    def completion(self):
        if self.ycor() > FINISH_LINE_Y :
            return True
        return False