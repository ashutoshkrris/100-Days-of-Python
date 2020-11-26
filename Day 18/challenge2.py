from turtle import Turtle, Screen

tim = Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
