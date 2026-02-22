def menu(): #menu
    menu = [
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Result",
        "6. Clear Result",
        "7. Exit"
    ]

    for each_option in menu:
        print(each_option)


def read_number(): #pedir numeros
    while True:
        try:
            number = float(input("Enter a number: ")) 
            return number
        except ValueError:
            print("Error, only negative, positive, and decimal numeric values ​​are accepted.")


def read_menu_option(): #validar opciones de menu
    while True:
        try:
            options = int(input("Select an option from the menu: "))
            return options
        except ValueError:
                print("Error, you must enter a valid number from the menu.")

def addition(first_number, second_number):
    result = first_number + second_number
    return result

def Subtraction(first_number, second_number):
    result = first_number - second_number
    return result

def Multiplication(first_number, second_number):
    result = first_number * second_number
    return result

def Division(first_number, second_number):
            result = first_number / second_number
            return result

def main():
    first_number = read_number()

    print("What do you want to do with the number?: ")
    menu()

    current_number = first_number

    options = 0
    while options != 7: 
        options = read_menu_option()
        if 1 <= options <= 4:
            second_number = read_number()

            if options == 1:
                current_number = addition(current_number, second_number)
                print(f"current result: {current_number}")
            elif options == 2:
                current_number = Subtraction(current_number, second_number)
                print(f"current result: {current_number}")
            elif options == 3:
                current_number = Multiplication(current_number, second_number)
                print(f"current result: {current_number}")

            if options == 4:
                if second_number == 0:
                    print("Invalid number, cannot be divided by 0.")
                    continue
                current_number = Division(current_number, second_number)
                print(f"current result: {current_number}")


        elif options == 5:
            print(current_number)
        elif options == 6:
            current_number = 0
            print("Result deleted. Current Value: 0")
        elif options == 7: 
            exit()
        else:
            print(("Number does not correspond to the menu."))



if __name__ == "__main__":
    main()
