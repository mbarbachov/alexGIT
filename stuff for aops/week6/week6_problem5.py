def is_multiple(x, y):
    """is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise"""
    # check if y divides evenly into x
    return x % y == 0


def is_prime(n):
    """is_prime(n) -> bool
    returns True if n is prime, False if n is not prime"""
    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n ** 0.5) + 1):
        if is_multiple(n, div):
            return False  # n isn't prime
    return True  # n is prime


def sum_of_primes(k):
    """sum_of_primes(k) -> int
    returns sum of the first k primes"""
    total = 0  # running total
    nextNumber = 2
    for i in range(k):
        while not is_prime(nextNumber):  # find the next prime
            nextNumber += 1
        total += nextNumber  # we found a prime, add it to the total
        nextNumber += 1
    return total


print(sum_of_primes(100))
