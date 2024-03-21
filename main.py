from turtle import Screen, Turtle
from random import randint

my_screen = Screen()
my_screen.setup(width=500, height=400)
colors = ["red", "green", "yellow", "blue", "orange", "purple"]

turtles = {}


def race_setup():
    num = -100
    for color in colors:
        num += 30
        turtles[color] = Turtle(shape="turtle")
        turtles[color].penup()
        turtles[color].color(color)
        turtles[color].goto(x=-230, y=num)


def race():
    user_choice = my_screen.textinput(title="Turtle Race!", prompt="Which color do you choose?: ")
    race_setup()

    while True:
        for turtle in turtles:
            turtles[turtle].forward(randint(1, 10))
            if turtles[turtle].xcor() >= 230:
                winning_turtle = turtle
                if user_choice == winning_turtle:
                    print(f"You win! The {winning_turtle} turtle won the race!")
                else:
                    print(f"You lost. The {winning_turtle} turtle won the race.")
                return


race()
my_screen.exitonclick()