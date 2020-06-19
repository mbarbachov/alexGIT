# ask for birth year,month, and day
year = int(input('What is the year the person was born? '))
month = int(input('What is the month the person was born? '))
day = int(input('What is the day the person was born? '))
# ask for current year,month, and day
year2 = int(input("What is the current year? "))
month2 = int(input("What is the current month? "))
day2 = int(input("What is the current day? "))


# we create the function
def mongo_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    # we convert the dates from the start into mongo terms
    birth_in_days = birth_year * 26 * 15 + birth_month * 26 + birth_day
    current_in_days = current_year * 26 * 15 + current_month * 26 + current_day

    # we subtract the two conversions
    difference = current_in_days - birth_in_days

    # we return the difference
    return '%.10f' % (difference / (26 * 15))


info = list(map(int, input('Enter the information for the age : ').split(',')))
print('The age of person on planet mongo is : ', mongo_age(info[0], info[1], info[2], info[3], info[4], info[5]))
