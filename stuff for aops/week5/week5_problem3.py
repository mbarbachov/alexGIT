scr = int(input("What is the score? "))


def assign_letter_grade(score):
    """Takes in a value score and returns a letter grade."""
    grade = ""
    if 96 <= score <= 100:
        # the grade is an A+
        grade += "A+"
    elif 88 <= score <= 95:
        # the grade is an A
        grade += "A"
    elif 85 <= score <= 87:
        # the grade is an B+
        grade += "B+"
    elif 80 <= score <= 84:
        # the grade is an B
        grade += "B"
    elif 77 <= score <= 79:
        # the grade is an C+
        grade += "C+"
    elif 70 <= score <= 76:
        # the grade is an C
        grade += "C"
    elif 66 <= score <= 69:
        # the grade is an D
        grade += "D"
    elif 50 <= score <= 65:
        # the grade is an F
        grade += "F"
    else:
        # the grade is an I
        grade += "I"
    return grade


print('The letter score is : ', assign_letter_grade(scr))
