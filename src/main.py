import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(1000, 700)

raceLine = Turtle("square", visible=False)
raceLine.penup()
raceLine.goto(300, 335)
raceLine.pendown()
raceLine.goto(300, -335)

turtleList = [
    Turtle("classic", visible=False),
    Turtle("classic", visible=False),
    Turtle("classic", visible=False),
    Turtle("classic", visible=False),
]

turtleColorList = [
    "blue",
    "yellow",
    "red",
    "pink",
]

for i in range(0, len(turtleList)):
    turtleList[i].penup()
    turtleList[i].color(turtleColorList[i])
    turtleList[i].goto(0, i * 50 - 100)
    turtleList[i].showturtle()

while True: #infinite loop
    for i in range(0, len(turtleList)):
        turtleList[i].forward(random.randint(1, 10))

        if turtleList[i].pos()[0] > 300:
            screen.exitonclick()

# my_turtle.color("blue")
# my_turtle.shapesize(5, 5)
# my_turtle.speed(1)
# my_turtle.penup()
# my_turtle.goto(500, 20)

# my_turtle.color("yellow")
# my_turtle.shapesize(2, 2)
# my_turtle.speed(1)
# my_turtle.penup()
# my_turtle.goto(500, 20)