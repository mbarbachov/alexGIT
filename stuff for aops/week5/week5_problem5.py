# Python Class 2402
# Lesson 5 Problem 5
# Author: gbtkalex (442655)
a = int(input('What is the first side? '))
b = int(input('What is the second side? '))
c = int(input('What is the third side? '))


def is_right_triangle(a, b, c):
    '''is_right_triangle(a,b,c) -> bool
    returns True if a,b,c is a right triangle with hypotenuse c'''
    if c > a and c > b:
        return a * a + b * b == c * c
    if a > c and a > b:
        return c * c + b * b == a * a
    if b > c and b > a:
        return c * c + a * a == b * b


if is_right_triangle(a, b, c) == True:
    print("Yes, it is a right triangle.")
else:
    print('No, it is not a right triangle.')
