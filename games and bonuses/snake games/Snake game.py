# we are using turtle instead of pyGame because it is easier
import turtle
# Importing time because we need a delay otherwise the program runs to fast
import time
# to help move the food to random spot
import random

# setting up the screen
wn = turtle.Screen()
wn.title("Snake Game!")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off screen updates

# Creating the snakeHead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# we are making a delay to make the program more user-friendly
delay = 0.1
delay -= 0.001

# scoring variables
score = 0
high_score = 0

# Snake food
# set up the food icon
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# making the snake Body.
segments = []

# Pen for the score
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# function gives the turtle the ability to move!
# The function only works though if the snake is pointing to some specific direction.
def move():
    """his function helps the turtle move around the screen"""
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()
    # Check for collision with border

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide segment when collision happens
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} apples  High score: {} apples".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))
    # check if touching food
    if head.distance(food) < 20:
        # move the food to a random spot on screen
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)
        # Increase score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} apples  High score: {} apples".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))
    # move the end in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # hide segment when collision happens
            for segment in segments:
                segment.goto(1000, 1000)
            # clear the segments list
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} apples  High score: {} apples".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)
wn.mainloop()
