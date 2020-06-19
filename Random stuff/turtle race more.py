import random
import turtle
import time

def backgammon_roll(n):
    x = random.randint(1, n)
    y = random.randint(1, n)
    if x != y:
        score = x + y
    else:
        score = 2 * (x + y)
    return score


turtle_count = 8
turtles = []
position = []
colors = ['red', 'blue', 'green', 'orange',"black","cyan","navy","lightgreen"]

for i in range(turtle_count):
    turtles.append(turtle.Turtle())
    position.append(0)
    turtles[i].shape('turtle')
    turtles[i].color(colors[i % len(colors)])
    turtles[i].penup()
    turtles[i].goto(0, 30 * i)


dani = turtle.Turtle()
dani.hideturtle()
wn = turtle.Screen()

race_is_over = False
while not race_is_over:
    for i in range(turtle_count):
        rolled = backgammon_roll(6)
        if rolled + position[i] > 300:
            rolled = 300 - position[i]
            race_is_over = True
        turtles[i].forward(2 * rolled)
        position[i] += rolled
    time.sleep(0.4)

# at this point race is over
winners_count = position.count(300)
if winners_count == 1:
    print("We have a clear winner!!!")
else:
    print("We have", winners_count, "winners!")

wn.mainloop()
