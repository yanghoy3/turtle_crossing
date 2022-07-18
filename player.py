from turtle import Turtle

STARTING_POSITION = (0, -285)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def turtle_position_reset(self):
        self.goto(STARTING_POSITION)

