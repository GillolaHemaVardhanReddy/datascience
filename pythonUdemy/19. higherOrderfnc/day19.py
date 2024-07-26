from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()

screen.listen() # now screen is listening


# scree.onkey(function,key) and screen.onkeyrelease(function,key)
# the function must have no arguments
# key must be like eg. "up","down","space","a" etc.. on keyboard

def moveforward():
    pencil.forward(10)

screen.onkey(key="space",fun=moveforward)  # when passing a function to other we just pass its name
screen.exitonclick()