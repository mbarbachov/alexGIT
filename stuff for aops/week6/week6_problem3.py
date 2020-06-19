# Python Class 2402
# Lesson 6 Problem 3
# Author: gbtkalex (442655)

import turtle
import random

wn = turtle.Screen()
alex = turtle.Turtle()


def random_walk(t, steps):
    t.speed(0)
    for i in range(steps):
        x = random.randrange(1, 51)
        t.forward(x)
        t.left(random.randrange(1, 361))


random_walk(alex, 10390190)

wn.mainloop()
