def triangular(m):
    '''triangular(m) -> int
    returns smallest triangular number >= m'''
    triNumber = 0  # keeps track of the triangular numbers
    nextInt = 1  # keeps track of the next integer to add
    while triNumber < m:
        triNumber += nextInt  # add the next integer, making the next tri number
        nextInt += 1  # go to the next integer
    return triNumber


print(triangular(100000))
