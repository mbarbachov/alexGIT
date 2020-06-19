# Python Class 2402
# Lesson 4 Problem 5 part (a)
# Author: gbtkalex (442655)
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()


def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


draw_square(tess, 50)

wn.mainloop()