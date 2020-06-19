for n in range(110,1000,11):  # check each possibility
    # grab the digits of n
    hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10
    # check if n/11 is the sum of the squares of the digits
    if n // 11 == hundreds**2 + tens**2 + ones**2:
        print(n)