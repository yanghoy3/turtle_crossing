from turtle import Turtle
FONT = ("Courier", 18, "normal")
FONT2 = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.display_level()
        goal = Turtle()
        # goal.color("red")
        goal.hideturtle()
        goal.penup()
        goal.goto(0, 260)
        goal.write("GOAL", align='center', move=False, font=FONT2)

    def display_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write("GAME OVER", align='center', move=False, font=FONT)
