from turtle import Screen
from Player import Player
from Car import Cars
from ScoreBoard import Scoreboard
import time

player = Player()
car = Cars()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

def Move_Up() :
    player.forward(10)

screen.listen()
screen.onkey(Move_Up,"Up")

game_is_on = True
while game_is_on :
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    for cars in car.all_cars :
        if cars.distance(player) < 20 :
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line() :
        player.goto(0,-280)
        scoreboard.increase_level()
        car.level_up()






screen.exitonclick()