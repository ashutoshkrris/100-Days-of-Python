from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("BREAKOUT")
screen.tracer(0)


def create_bricks():
    gang_of_bricks = []
    colors = ["red", "orange", "green", "yellow"]
    for lines in range(4):
        x_pos = -380
        y_pos = 230 - (lines * 30)
        color = colors[lines]
        for n in range(2):
            for i in range(14):
                gang_of_bricks.append(
                    Brick(color=color, x_pos=x_pos + (i * 57), y_pos=y_pos - (n * 15)))
    return gang_of_bricks


paddle = Paddle((0, -230))
ball = Ball()
scoreboard = Scoreboard()
bricks = create_bricks()
sleep_time = 0.02

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -210:
        ball.bounce_y()

    # Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position()
        sleep_time = 0.02

    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 20:
            brick.hideturtle()
            bricks.remove(brick)

            # Points
            if brick.color()[0] == "yellow":
                scoreboard.point(1)
            elif brick.color()[0] == "green":
                scoreboard.point(3)
            elif brick.color()[0] == "orange":
                scoreboard.point(5)
            elif brick.color()[0] == "red":
                scoreboard.point(7)

            # Work out which way to bounce... needs a LOT of work...
            if abs(brick.ycor() - ball.ycor()) < 5 and abs(brick.xcor() - ball.xcor()) > 10:
                ball.bounce_x()
            if abs(brick.xcor() - ball.xcor()) < 20:
                ball.bounce_y()

            # Increment speed
            if sleep_time > 0.001:
                sleep_time -= 0.0005

screen.exitonclick()
