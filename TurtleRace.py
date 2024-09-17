import turtle as t
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
Bet = screen.textinput(title="Make your bet!" , prompt="Which turtle do you think will win? Enter a color : ")

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.penup()
turtle1.goto(x=-230,y=-150)

turtle2 = Turtle()
turtle2.shape("turtle")
turtle2.color("green")
turtle2.penup()
turtle2.goto(x=-230,y=-100)

turtle3 = Turtle()
turtle3.shape("turtle")
turtle3.color("blue")
turtle3.penup()
turtle3.goto(x=-230,y=-50)

turtle4 = Turtle()
turtle4.shape("turtle")
turtle4.color("orange")
turtle4.penup()
turtle4.goto(x=-230,y=0)

turtle5 = Turtle()
turtle5.shape("turtle")
turtle5.color("yellow")
turtle5.penup()
turtle5.goto(x=-230,y=50)

turtle6 = Turtle()
turtle6.shape("turtle")
turtle6.color("violet")
turtle6.penup()
turtle6.goto(x=-230,y=100)

turtles = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6]

a = True
while a == True :
    for item in turtles :
        random_num = random.randint(0,10)
        item.forward(random_num)
        if item.xcor() > 230 :
            Winner = item
            if Winner == Bet :
                print("You Win.")
            else :
                print("You Lose.")
            a = False



print(turtle1)
print(turtle2)
print(turtle3)
print(turtle4)
print(turtle5)
print(turtle6)