from turtle import Turtle

def createsnake():
    """this function creates a snake with 3 segments and returns a list of turtle segements which is represented as snake"""
    start_pos = [(0,0),(-20,0),(-40,0)]
    snake = []
    for item in start_pos:
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()  # Lift the pen to prevent drawing lines
        segment.goto(item)
        snake.append(segment)  # Add the segment to the snake list
    return snake

def movesnake(snake):
    """this move snake is used to move the snake forward irrespective of direction"""
    for i in range(len(snake)-1,0,-1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x,y)
    snake[0].forward(20)

def changedirection(snake,direction):
    """this function helps us change the direction of the snake"""
    snake.setheading(direction)
    movesnake(snake)