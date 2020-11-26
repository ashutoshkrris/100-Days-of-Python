from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class"""

    def __init__(self):
        """Constructor"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Method to create snake"""
        for i in STARTING_POSITIONS:
            new_part = Turtle('square')
            new_part.color('white')
            new_part.penup()
            new_part.goto(i)
            self.segments.append(new_part)

    def move(self):
        for part in range(len(self.segments)-1, 0, -1):
            self.segments[part].goto(
                self.segments[part-1].xcor(), self.segments[part-1].ycor())
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
