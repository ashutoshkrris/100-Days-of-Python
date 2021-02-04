from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
        self.penup()
        self.goto(x_pos, y_pos)
