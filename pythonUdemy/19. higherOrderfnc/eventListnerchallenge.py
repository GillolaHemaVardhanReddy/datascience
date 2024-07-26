logo = """
  ______ _       _                       _____ _        _       _     
 |  ____| |     | |           /\        / ____| |      | |     | |    
 | |__  | |_ ___| |__ ______ /  \ _____| (___ | | _____| |_ ___| |__  
 |  __| | __/ __| '_ \______/ /\ \______\___ \| |/ / _ \ __/ __| '_ \ 
 | |____| || (__| | | |    / ____ \     ____) |   <  __/ || (__| | | |
 |______|\__\___|_| |_|   /_/    \_\   |_____/|_|\_\___|\__\___|_| |_|
                                                                      
                                                                      
"""

from turtle import Turtle, Screen

print(logo)

pencil = Turtle()
screen = Screen()

screen.listen() 

def moveforward():
    pencil.forward(10)

def movebackward():
    pencil.backward(10)

def movelef():
    pencil.setheading(pencil.heading()+10)


def moveright():
    pencil.setheading(pencil.heading()-10)

def clearall():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()

screen.onkey(key="w",fun=moveforward)
screen.onkey(key="s",fun=movebackward)
screen.onkey(key="a",fun=movelef)
screen.onkey(key="d",fun=moveright)
screen.onkey(key="c",fun=clearall)


screen.exitonclick()