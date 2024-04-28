import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_coors = data.x.to_list()
y_coors = data.y.to_list()
missed_states = {
    "state": [],
    "x": [],
    "y": []
}
correct_guess = []

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What is the another state's name?").title()

    if answer == "Exit":
        for i in range(0, len(states) - 1):
            if states[i] not in correct_guess:
                missed_states["state"].append(states[i])
                missed_states["x"].append(x_coors[i])
                missed_states['y'].append(y_coors[i])
            else:
                pass

        missed_states_csv = pandas.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break

    if answer in states and answer not in correct_guess:
        correct_guess.append(answer)
        state_index = states.index(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_coors[state_index], y_coors[state_index])
        t.write(arg=answer, move=False, align="center", font=("Courier", 8, "bold"))
    else:
        pass

if len(correct_guess) == 50:
    turtle.home()
    turtle.write(arg="Well Done. You have written all States.🎉🎉", move=False, align="center", font=("Courier", 15, "bold"))
