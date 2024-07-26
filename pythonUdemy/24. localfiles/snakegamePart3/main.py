from turtle import Turtle,Screen
from methods import createsnake,movesnake
from snakeclass import Snake
from screenclass import ScreenCtrl
from foodclass import Food
from scoreboard import Score

screen = ScreenCtrl()

snake = Snake()

snake.changedirection()

active = True
food = Food()
score = Score()

while(active):
    screen.updatechange()
    snake.move()

    # detect if snake eats food
    if snake.segments[0].distance(food) < 15 :
        food.regenerate()
        snake.extend()
        score.incscore()

    # boundary detection
    if snake.detectboundary() :
        score.reset()
        snake.reset()

    # self collision detection
    if snake.detectselfcollision() :
        score.reset()
        snake.reset()

screen.exitcondition()