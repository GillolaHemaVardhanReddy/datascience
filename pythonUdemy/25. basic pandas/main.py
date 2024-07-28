import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. states games")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# def getmouseclick(x, y):
#     print(x, y)

# turtle.onscreenclick(getmouseclick)
# turtle.mainloop()

statelist = pd.read_csv("50_states.csv")

allstates = statelist.state.to_list()

guessed = []
while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50", prompt="What's another state name").title()
    if answer == 'Exit':
        missing = []
        for state in allstates:
            if state not in guessed:
                missing.append(state)
        print(missing)
        newdata = pd.DataFrame(missing)
        newdata.to_csv("states_to_learn.csv")
        break
    if answer in allstates:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        statedata = statelist[statelist["state"]==answer]
        t.goto(statedata.x.item(),statedata.y.item())
        t.write(answer)
