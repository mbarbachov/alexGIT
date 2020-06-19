letter = str(input('Type the letter you want to make a letter square out of : '))
side_length = int(input('Type the side length for the letter square : '))


def letter_square(letter, size):
    my_string = ""
    for i in range(size):
        my_string = my_string + str(letter) * size + '\n'

    my_string = my_string[:-1]
    return my_string


print(letter_square(str(letter), int(side_length)))