from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.car_list = []
        self.STARTING_MOVE_DISTANCE = 5
        for i in range(30):
            self.car_initial_setup()

    def car_initial_setup(self):
        tim = Turtle()
        tim.speed("fastest")
        tim.penup()
        tim.shape("square")
        tim.turtlesize(1, 2)
        tim.color(random.choice(COLORS))
        tim.goto(random.randint(-30, 30)*10, -240 + random.randint(0, 12) * 40)
        tim.setheading(180)
        self.car_list.append(tim)

    def generate_cars(self):
        tim = Turtle()
        tim.speed("fastest")
        tim.penup()
        tim.shape("square")
        tim.turtlesize(1, 2)
        tim.color(random.choice(COLORS))
        tim.goto(300, -240 + random.randint(0, 12) * 40)
        tim.setheading(180)
        self.car_list.append(tim)

    def move_cars(self):
        for i in range(len(self.car_list)):
            self.car_list[i].forward(self.STARTING_MOVE_DISTANCE)

    def increase_difficulty(self):
        self.STARTING_MOVE_DISTANCE += 2


