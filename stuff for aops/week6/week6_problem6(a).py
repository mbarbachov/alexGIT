# Python Class 2402
# Lesson 6 Problem 6 part (a)
# Author: gbtkalex (442655)

import random


def backgammon_roll(n):
    x = random.randint(1,n)
    y = random.randint(1,n)
    print('Your first dice roll is : ', int(x))
    print('Your second dice roll is : ', int(y))
    if x != y:
        score = x + y
        print("Your score is :", str(score))
    elif x == y:
        score = 2 * (x + y)
        print("Your score is : ", str(score))


backgammon_roll(6)