from screenclass import ScreenCtrl
from paddleclass import Paddle
from ballclass import Ball
from scoreclass import Score

screen = ScreenCtrl()
player1 = Paddle((350,0))
player2 = Paddle((-350,0))
ball = Ball()
score = Score()


game_is_on = True
while game_is_on:
    screen.updatechange(ball.speedy)
    screen.keyboardctrl(player1,player2)
    ball.move()
    
    # detect any collision
    ball.detectcollision(player1,player2)

    # detech if player misses ball
    if ball.xcor() > 380 :
        ball.resetposition()
        score.l_point()

    if ball.xcor() < -380:
        ball.resetposition()
        score.r_point()


screen.exitcondition()