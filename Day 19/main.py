from turtle import Turtle, Screen

turty = Turtle()
screen = Screen()


def move_forward():
    turty.forward(10)


screen.listen()
screen.onkey(move_forward, 'space')

screen.exitonclick()