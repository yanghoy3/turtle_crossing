import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

road = Road()
car = CarManager()
car.car_initial_setup()
tim = Player()
scoreboard = Scoreboard()
level = 3

screen.listen()
screen.onkey(tim.move, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.move_cars()
    screen.update()

    if random.randint(0, level) == 0:
        car.generate_cars()

    if tim.ycor() > 260:
        scoreboard.next_level()
        tim.turtle_position_reset()
        car.increase_difficulty()
        if level > 0:
            level -= 1

    for i in range(len(car.car_list)):
        if tim.distance(car.car_list[i]) < 33:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
