from turtle import Turtle, Screen

tim = Turtle()

########### Challenge 3 - Draw Shapes ########

colors = ["cornflower blue", "aquamarine", "gold", "dark red",
          "salmon", "indigo", "dark green", "gray", "olive drab", "olive"]


def draw_shapes(n):
    for _ in range(n):
        tim.forward(100)
        tim.right(360//n)


for i in range(3, 11):
    tim.color(colors[i-3])
    draw_shapes(i)


screen = Screen()
screen.exitonclick()
