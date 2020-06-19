import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("red")
tess.penup()
tess.goto(-1250, 0)
tess.speed(0)
tess.hideturtle()
tess.pendown()


def draw_bar(t, height):
    t.speed(0)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)


xs = [92,
      38,
      167,
      149,
      17,
      110,
      11,
      69,
      109,
      159,
      28,
      89,
      188,
      85,
      109,
      194,
      95,
      30,
      147,
      144,
      121,
      136,
      113,
      144,
      142,242,
470,
503,
504,
432,
247,
670,
551,
375,
274,
619,
284,
332,
277,
420,
249,
289,
386,
492,
336,
452,
382,
492,
650,
598]
for v in xs:
    if v >= 200:
        tess.color('green')
        draw_bar(tess, v)
    else:
        tess.color('red')
        draw_bar(tess, v)

wn.mainloop()
