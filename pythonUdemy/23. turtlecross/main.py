from playerclass import Player
from carclass import Car
from scoreclass import Score
from screenclass import ScreenCtrl

screen = ScreenCtrl()
player = Player()
car = Car()

game_is_on = True
time = 0
score = Score()

while game_is_on:
    screen.updatechange(0.1)
    if(time>40):
        car.writestart(time)
        screen.keyboardctrl(player)
    time+=1
    car.createcar()
    car.move()

    # collision detection
    if player.collision(car.cars):
        car.write("Game Over!")
        game_is_on = False
    
    # successful completion of level
    if player.completion():
        player.gotostart()
        car.levelup()
        score.updatelevel()


screen.exitcondition()