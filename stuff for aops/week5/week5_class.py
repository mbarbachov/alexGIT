def is_multiple(x, y):
    if x % y == 0:
        print(str(x), "is a multiple", str(y))
    else:
        print(str(x), "is not a multiple of", str(y))


def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    # check every divisor from 2 up to sqrt(n)
    if n < 2:
        return False

    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


prime_counter = 0
prime_sum = 0
next_number = 0
while prime_counter < 100:
    if is_prime(next_number):
        print('Count:', prime_counter, 'Value:', next_number)
        prime_sum += next_number
        prime_counter += 1
    next_number += 1

print(prime_sum)
