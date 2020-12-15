import pandas as pd
import turtle

from pandas._libs import missing

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data using pandas
data = pd.read_csv("50_states.csv")
states = data.state.tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer_text = screen.textinput(
        title=f"{len(guessed_states)}/50 correct", prompt="What's another state name?")

    answer_text = answer_text.capitalize()

    if answer_text == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_text in states:
        guessed_states.append(answer_text)
        turty = turtle.Turtle()
        turty.hideturtle()
        turty.penup()
        coor = data[data.state == answer_text]
        turty.goto(int(coor.x), int(coor.y))
        turty.write(answer_text)

