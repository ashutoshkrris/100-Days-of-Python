from turtle import Turtle, Screen
from random import randint

is_race_started = False

# Screen
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(
    title="Make your bet!", prompt="Which turtle will win the race? Enter the color : ")

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

# Turtles
for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-235, y_positions[i])
    all_turtles.append(new_turtle)

if user_input:
    is_race_started = True

while is_race_started:

    for turtle in all_turtles:

        if turtle.xcor() > 215:
            is_race_started = False
            winner_color = turtle.pencolor()

            if winner_color == user_input:
                print(f"Yay! you and your {user_input} turtle won the race.")
            else:
                print(
                    f"Oops! you and your {user_input} turtle couldn't win the race.")
                print(f"The winner is {winner_color} turtle.")

        turtle.forward(randint(1, 10))

# screen.exitonclick()
