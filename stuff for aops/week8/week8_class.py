def longest_word_length(string):
    word_list = string.split()
    max_length = 0
    word1 = ''
    for word in word_list:
        word1 = word
        if len(word1) > max_length:
            max_length = len(word1)
    return max_length and word1


def write_digits_numbers():
    digits = [2, 3, 5, 7]
    for tens in digits:
        for ones in digits:
            print(10 * tens + ones)


def class_stuff():
    pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 4]
    print(pi[2:7])  # prints the numbers between making 7-2 = 5 elements
    print(pi[0:5])  # prints the first five numbers
    print(pi[:5])  # also works
    print(pi[5:])  # prints the last five
    print(list(range(1, 9, 2)))
    print(pi[1:9:2])


def stuff():
    myList = [1, 1, 2, 3, 5]
    print(myList)
    myList.extend([8, 13])
    print(myList)
    myList.insert(4, 200)
    print(myList)


def plus_minus_one(x):
    """plus_minus_one(num) -> num, num
    Returns numbers one higher and one lower than the input."""
    oneHigher = x + 1
    oneLower = x - 1
    return oneHigher, oneLower
