# Python Class 2402
# Lesson 6 Problem 7
# Author: gbtkalex (442655)

import random


def guessing_game(n):
    num = random.randrange(1, 101)
    guess = -1

    num_of_tries = 0
    while num != guess:
        guess = int(input("What is your guess? "))
        if guess < num:
            print("That is lower than my number.")
            num_of_tries += 1
        elif guess > num:
            print("That greater than my number.")
            num_of_tries += 1
        else:
            print("Congratulations you have guessed my number!")
            print('The number was :', str(num))
            return num_of_tries


guesses = guessing_game(100)
print("It took you " + str(guesses) + " guesses.")
