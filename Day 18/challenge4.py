import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

tim.speed('fastest')

while True:
    tim.color(random.choice(colours))
    tim.pensize(10)
    tim.forward(20)
    tim.setheading(random.choice(directions))

