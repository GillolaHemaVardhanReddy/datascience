from turtle import Turtle,Screen
from methods import createsnake,movesnake
from snakeclass import Snake
from screenclass import ScreenCtrl

screen = ScreenCtrl()

snake = Snake()

snake.changedirection()

active = True

while(active):
    screen.updatechange()
    snake.move()
    
    

screen.exitcondition()