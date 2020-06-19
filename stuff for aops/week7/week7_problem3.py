def make_acronym(string):
    # split the string to seperate letters
    split_string = string.split()
    # setting the acronym to empty string
    acronym = ""
    for i in split_string:
        if i[0].isupper():
            acronym = acronym + i[0].upper()
        else:
            acronym = acronym + i[0].lower()

    return acronym


string = str(input("What string do you want acronymize? "))
print(make_acronym(string))
