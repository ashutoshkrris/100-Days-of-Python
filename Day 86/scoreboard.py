from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 230)
        self.write(self.score, align="center", font=("Courier", 70, "normal"))

    def point(self, points):
        self.score += points
        self.update_scoreboard()
