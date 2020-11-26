from turtle import Turtle, Screen
import time

# Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Snake Body
# part_1 = Turtle('square')
# part_1.color('white')

# part_2 = Turtle('square')
# part_2.color('white')
# part_2.goto(-20,0)

# part_3 = Turtle('square')
# part_3.color('white')
# part_3.goto(-40,0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for i in range(3):
    new_part = Turtle('square')
    new_part.color('white')
    new_part.penup()
    new_part.goto(starting_pos[i])
    snake.append(new_part)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for part in range(len(snake)-1, 0, -1):
        snake[part].goto(snake[part-1].xcor(), snake[part-1].ycor())
    snake[0].forward(20)


screen.exitonclick()
