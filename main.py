from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []

x = -230
y = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    all_turtle.append(new_turtle)

if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("Congratulations!! Your turtle won")
            else:
                print(f"Sorry!! {winning_colour} turtle won the race")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
