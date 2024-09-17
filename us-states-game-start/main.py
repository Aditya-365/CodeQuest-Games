import turtle
import pandas 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Adi/PythonCodes/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#  The code below is to find out the (x,y) coordinates of a mouse click on a image(here, a country.)...
# def get_mouse_click_coor(x,y) :
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states_guessed_correctly = 0
guessed_states = []
while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{states_guessed_correctly}/50 Guessed" , prompt="What's another state's name? ").title()
    data = pandas.read_csv("/Adi/PythonCodes/us-states-game-start/50_states.csv")
    all_states = data["state"].to_list()
    if answer_state.lower() == "exit" :
        missing_states = []
        for i in all_states :
            if i not in guessed_states :
                missing_states.append(i)
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("/Adi/PythonCodes/us-states-game-start/States_to_learn.csv")
        break
    for i in all_states :
        if answer_state == i :
            states_guessed_correctly += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == answer_state]
            t.goto(int(state_data["x"]),int(state_data["y"]))
            t.write(answer_state)
            guessed_states.append(answer_state)


screen.exitonclick()