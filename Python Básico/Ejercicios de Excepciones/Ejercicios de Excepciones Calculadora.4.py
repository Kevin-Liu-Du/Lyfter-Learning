def menu():
    menu = {
            1: "Addition",
            2: "Subtraction",
            3: "Multiplication",
            4: "Division",
            5: "Result",
            6: "Clear Result",
            7: "Exit",
        }

    for number, options in menu.items():
        print(f"{number}. {options}")

    return menu

def read_number():
    while True:
        try:
            number = float(input("Enter a number: ")) 
            return number
        except ValueError:
            print("Error, only negative, positive, and decimal numeric values ​​are accepted.")


def read_menu_option(): 
    while True:
        try:
            options = int(input("Select an option from the menu: "))
            return options
        except ValueError:
                print("Error, you must enter a valid number from the menu.")


def addition(first_number, second_number):
    result = first_number + second_number
    return result

def subtraction(first_number, second_number):
    result = first_number - second_number
    return result

def multiplication(first_number, second_number):
    result = first_number * second_number
    return result

def division(first_number, second_number):
    result = first_number / second_number
    return result


def main():
    first_number = read_number()
    current_number = first_number
    print("What do you want to do with the number?: ")

    returned_menu = menu() #I call the function and when the function returns something, it needs to be caught somewhere.
    options = returned_menu.keys() #(1234567)

    selected_options = 0

    while selected_options != 7:
            # if selected_options == 7: 
            #     exit()

            selected_options = read_menu_option() # el numero que ingresa el usuario
            if selected_options not in options:
                    print("Number does not correspond to the menu.")
                    continue

            if 1 <= selected_options <= 4:
                second_number = read_number()

                if selected_options == 1:
                    addition_result = addition(current_number, second_number)
                    print(f"Current result: {addition_result}")
                    current_number = addition_result
                elif selected_options == 2:
                    subtraction_result = subtraction(current_number, second_number)
                    print(f"Current result: {subtraction_result}")
                    current_number = subtraction_result
                elif selected_options == 3:
                    multiplication_result = multiplication(current_number, second_number)
                    print(f"Current result: {multiplication_result}")
                    current_number = multiplication_result
                elif selected_options == 4:
                    while second_number == 0:
                        print("Invalid number, cannot be divided by 0.")
                        second_number = read_number()

                    division_result = division(current_number, second_number)
                    print(f"Current result: {division_result}")
                    current_number = division_result

            if selected_options == 5:
                print(f"Current result: {current_number}")

            if selected_options == 6:
                current_number = 0
                print("Calculator cleared. Current result is 0.")








if __name__ == "__main__":
    main()

