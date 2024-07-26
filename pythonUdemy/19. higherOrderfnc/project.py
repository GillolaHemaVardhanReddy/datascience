# understanding turtle coordinate system

from turtle import Turtle,Screen
import random as rd
import turtle

screen = Screen()
colors = ["red","orange","yellow","green","blue","purple"]

# screen.setup(width,height)
screen.setup(500, 400)

# take input like textinput(title,prompt), numinput(title,prompt)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter a color: ")

# coordinate system in turtle is like
    # initially turtle lies at center at x=0 and y=0
    # if we have width 200 and height 200 then 
        # from center to top height is 100 and center to bottom its again 100 (till -100)
        # from center to right its +ve and size 100 and center to leftits --ve and size 100

yaxis = [-100,-60,-20,20,60,100]
is_race = False
pens = []

for i in range(6):
    pen = Turtle(shape="turtle")
    pen.color(colors[i])
    pen.penup()
    pen.goto(-240,yaxis[i])
    pens.append(pen)

if user_bet:
    is_race = True

winner = ""
while is_race:
    for pen in pens:
        if pen.xcor() > 230 :
            winner = pen.pencolor()
            is_race = False
        d = rd.randint(0,10)
        pen.forward(d)

common = f"{winner} color turtle is winner"

if winner == user_bet :
    print("Yay you won "+common)
else:
    print("Sorry you lost "+common)

screen.exitonclick()