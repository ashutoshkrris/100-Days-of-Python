#####Turtle Intro######

import turtle as t

turty = t.Turtle()
turty.shape("turtle")
turty.color("red")
# turty.forward(100)
# turty.backward(200)
# turty.right(90)
# turty.left(180)
# turty.setheading(0)


######## Challenge 1 - Draw a Square ############
for _ in range(4):
    turty.forward(100)
    turty.left(90)


screen = t.Screen()
screen.exitonclick()
print("Bye!")