def validate_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("You must enter a valid number.")


def validate_name(message):
    while True:
        name = input(message)
        if name.replace(" ", "").isalpha():
            return name
        print("You must enter letters and spaces only.")


def validate_grade(message):
    while True:
        try:
            grade = float(input(message))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("You must enter a valid number.")

def validate_section(message):
    while True:
        section = input(message).strip() #Remove spaces at the beginning and end.

        if (
            len(section) >= 2 and #Verify that the section has at least 2 characters, as it requires at least 1 letter and 1 number. 
            section[:-1].isdigit() and #section[:-1] takes all characters of the section except the last one, and checks if they are digits.
            section[-1].isalpha() #section[-1] takes the last character of the section and checks if it is a letter.
        ):
            return section.upper()
        
        print("Class number must be like 11B (numbers followed by one letter).")
