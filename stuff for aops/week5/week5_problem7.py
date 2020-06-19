def sum_of_proper_divs(n):
    sum_is = 0
    for i in range(1, n):
        if n % i == 0:
            if n % i == n:
                sum_is += 0
            sum_is += i
    return sum_is


for i in range(1, 10000):
    if sum_of_proper_divs(i) == i:
        print(str(i), "is a perfect number!")


def is_perfect_number(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors == number


for i in range(100, 1000):
    if is_perfect_number(i):
        print(str(i), "is a perfect number!")
