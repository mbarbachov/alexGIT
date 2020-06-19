import random
import time

P1score = 0
P2score = 0


def backgammon_roll(n):
    x = random.randint(1, n)
    y = random.randint(1, n)
    if x != y:
        score = x + y
    else:
        score = 2 * (x + y)
    return score


while P1score < 300 and P2score < 300:
    rolled1 = backgammon_roll(6)
    rolled2 = backgammon_roll(6)

    print("Player 1 rolled :", int(rolled1))
    print("Player 2 rolled :", int(rolled2))

    P1score += rolled1
    P2score += rolled2
    print("Player 1 has :", P1score, "points.", "Player 2 has :", int(P2score), "points.")

if P1score < P2score:
    print("Player 2 wins!")
elif P1score > P2score:
    print("Player 1 wins!")

else:
    print("It is a Draw!")
