print('I will convert hours + minutes + seconds into seconds')
hours = int(input('How many hour(s)? '))
minutes = int(input("How many minute(s)? "))
seconds = int(input('How many second(s)? '))


def convert_to_seconds(h, m, s):
    return s + 60 * m + 3600 * h


print('The number of seconds is :', int(convert_to_seconds(hours, minutes, seconds)))
