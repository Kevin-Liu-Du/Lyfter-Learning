

def ask_name():
    while True:
        try:
            name = input("Enter your name: ")
            if name.isdigit():
                raise ValueError()
            return name
        except ValueError:
            print("The name cannot be a number")

#ask_name()

def ask_age():
    while True:
        try:
            age = input("Enter your age: ")
            if not age.isdigit():
                raise ValueError()
            return age
        except ValueError as error:
            print("Invalid number")
            #print(error)

#ask_age()

name = ask_name()
age = ask_age()

print(f"Hello {name}, your age is {age}")