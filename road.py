from turtle import Turtle


class Road:

    def __init__(self):
        self.road_marking()
        self.pond()

    def road_marking(self):
        for i in range(18):
            road = Turtle()
            road.shape("square")
            road.color("white")
            road.penup()
            road.turtlesize(0.1, 30)
            road.goto(0, -260+i*40)

    def pond(self):
        for i in range(1):
            pond = Turtle()
            pond.shape("square")
            pond.color("blue")
            pond.penup()
            pond.turtlesize(2.2, 30)
            pond.goto(0, -284+i*560)

