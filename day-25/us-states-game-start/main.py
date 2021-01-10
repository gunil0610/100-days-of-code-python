import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

answer_list = []

while len(answer_list) < 50:
    answer_state = screen.textinput(
        title="Guess the State", prompt=f"{len(answer_list)}/50 States Correct").title()

    if answer_state == 'Exit':
        missing_states = [
            state for state in states_list if state not in answer_list]

        # for state in states_list:
        #     if state not in answer_list:
        #         missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in answer_list:
        x_cor = int(data[data.state == answer_state].x)
        y_cor = int(data[data.state == answer_state].y)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.ht()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(answer_state, align="center")
        answer_list.append(answer_state)
