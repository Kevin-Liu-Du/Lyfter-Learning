def menu():
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


def read_number(): 
    while True:
        try:
            first_number = float(input("Enter a random number: ")) 
            return first_number
        except ValueError:
            print("Error, only negative, positive, and decimal numeric values ​​are accepted.")


def read_menu_option():
    while True:
        try:
            options = int(input("Select an option from the menu: "))
            return options
        except ValueError:
                print("Error, you must enter a valid number from the menu.")

# def read_second_number():
#     while True:
#         try:
#             second_number = float(input("Enter a random number: "))
#             return second_number
#         except ValueError:
#             print("Error, only negative, positive, and decimal numeric values ​​are accepted.")
            

first_number = read_number()

print("What do you want to do with the number?: ")
menu()

current_number = first_number

options = 0
while options != 7: 
    options = read_menu_option()
    if 1 <= options <= 4:
        second_number = read_number() #That would make sense; it has to ask for another number, which is the same function as at the beginning. 

        if options == 4:
            if second_number == 0:
                print("Invalid number, cannot be divided by 0.")
                continue

        if options == 1:
            current_number += second_number
            print(current_number)
        elif options == 2:
            current_number -= second_number
            print(current_number)
        elif options == 3:
            current_number *= second_number
            print(current_number)
        elif options == 4:
            current_number /= second_number
            print(current_number)



    elif options == 5:
        print(current_number)
    elif options == 6:
        current_number = 0
        print(f"Result deleted. Current Value: {current_number}")
    elif options == 7:
        exit()
    else:
        print(("Number does not correspond to the menu."))


#porcentajes
#raiz cuadrada
#potencia
