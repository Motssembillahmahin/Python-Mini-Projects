import pandas as pd
import turtle
guessed_state = []
screen = turtle.Screen()
screen.title('U.S state checker')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('50_states.csv')
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 states count', prompt='Whats another state name')


    def similarity():
        for i in data.state:
            if i.capitalize() == answer_state.capitalize():
                obtain_value = data[data.state == i]
                x = obtain_value.iloc[0, 0]
                guessed_state.append(x)
                print(x)
                print(guessed_state)
                print(len(guessed_state))
        return int(obtain_value.iloc[0, 1]), int(obtain_value.iloc[0, 2])
        # print(answer_state)


    # print(guessed_state)
    coordinate = list(similarity())
    location = data[(data.x == coordinate[0]) & (data.y == coordinate[1])]


    def turtle_part():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(coordinate[0], coordinate[1])
        t.write(location.state.item())


    turtle_part()

screen.exitonclick()
