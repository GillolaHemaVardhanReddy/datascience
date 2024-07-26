from turtle import Turtle,Screen
distance = 20
start_pos = [(0,0),(-20,0),(-40,0)]
screen = Screen()

class Snake:
    """
        1. this class is used to define a snake
        2. createsnake method used to create snake with 3 segments
        3. move snake moves the snake by distance
    """

    def __init__(self):
        self.segments = []
        self.createsnake()

    def createsnake(self):
        """
            this function creates a snake with 3 segments and returns a list of turtle segements 
            which is represented as snake
        """
        for item in start_pos:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()  # Lift the pen to prevent drawing lines
            segment.goto(item)
            self.segments.append(segment)  # Add the segment to the snake list
    
    def move(self):
        """this move snake is used to move the snake forward irrespective of direction"""
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(distance)

    def left(self):
        """this function changes snakes direction to left"""
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        """this function changes snakes direction to right"""
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def up(self):
        """this function changes snakes direction to up"""
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        """this function changes snakes direction to down"""
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def changedirection(self):
        """this function changes snakes direction according to keyboard press"""
        screen.onkeypress(self.left,"Left")
        screen.onkeypress(self.right,"Right")
        screen.onkeypress(self.up,"Up")
        screen.onkeypress(self.down,"Down")
    
