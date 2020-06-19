# Python Class 2402
# Lesson 4 Problem 5 part (a)
# Author: gbtkalex (442655)
import turtle

num = int(input('How many squares for this temple?'))

wn = turtle.Screen()
tess = turtle.Turtle()
sz = 25


def draw_square(t, size):
    for j in range(4):
        t.forward(size)
        t.left(90)


tess.speed(0)
for i in range(num):
    tess.pendown()
    draw_square(tess, sz)
    sz = sz + 30
    tess.penup()
    tess.right(90)
    tess.forward(15)
    tess.left(90)
    tess.forward(-15)

wn.mainloop()
