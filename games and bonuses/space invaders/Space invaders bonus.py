import turtle
import math
import os
import platform
import time

if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Windows sound module not available")

style = ("Times new roman", 14, "normal")

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("back.gif")
wn.tracer(0)
wn.setup(715, 715)

# turtle.register_shape("all bonuses/invader.png")
turtle.addshape("invader.gif")
turtle.addshape("player.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.hideturtle()
border_pen.color("white")
border_pen.penup()
border_pen.goto(-315, -315)
border_pen.pensize(3)

score1 = 0
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(-290, 280)
score_string = "Score: %s " % score1
score.write(score_string, align="left", font=style)

player = turtle.Turtle()
player.color('blue')
# player.shape("player.jpg")
player.penup()
player.speed(0)
player.goto(0, -250)
player.left(90)

player.speed = 0
player.shape("player.gif")

number_of_enemies = 40
# create an empty list of enemies
enemies = []
# add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.turtlesize((1) / 2)
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.goto(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemy_speed = 0.2

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.left(90)
bullet.shapesize(0.5, 0.5)

bullet_speed = 7

#  define bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"


def move_left():
    player.speed = -3


def move_right():
    player.speed = 3


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # declare bullet_state as global if it needs to be changed
    global bullet_state
    if bullet_state == "ready":
        os.system("afplay laser.wav&")
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


def play_sound(sound_file, time=0):
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    else:
        os.system("afplay {}&".format(sound_file))
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))


# keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

style = ("Impact", 100, "normal")
while True:
    wn.update()
    move_player()
    for enemy in enemies:
        # moving enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # reverse at border
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1
        if is_collision(bullet, enemy):
            # reset the bullet
            os.system("afplay explode.wav&")
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            # reset the enemy
            enemy.hideturtle()
            enemy_speed += 0.15
            enemy.goto(0, 800)


            score1 += 10
            score_string = ("Score: %s" % score1)
            score.clear()
            score.write(score_string, align="left", font=("Times new roman", 14, "normal"))
        if is_collision(enemy, player):
            os.system("afplay explode.wav&")
            score.clear()
            enemy_speed = 1000
            enemy.hideturtle()
            player.hideturtle()
            bullet.hideturtle()
            border_pen.goto(0, 0)
            border_pen.write("Game", align="center", font=style)
            border_pen.goto(0, -100)
            border_pen.write("Over", align="center", font=style)
            break
        if score1 == 400:
            score.clear()
            enemy.hideturtle()
            player.hideturtle()
            bullet.hideturtle()
            border_pen.goto(0, 0)
            border_pen.write("You", align="center", font=style)
            border_pen.goto(0, -100)
            border_pen.write("Win", align="center", font=style)
            break

    # move the bullet
    if bullet_state == "ready":
        bullet.hideturtle()

    if bullet_state == "fire":
        bullet.showturtle()
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"


