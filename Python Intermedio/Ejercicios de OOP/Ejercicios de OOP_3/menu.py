def show_menu():
    print("\n=== MAIN MENU ===")
    print("1. Add students")
    print("2. View all students")
    print("3. View top 3 best averages")
    print("4. View average grade of all students")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Remove student")
    print("8. View failed students")
    print("9. Exit")


def obtain_option():
    while True:
        try:
            menu_option = int(input("Select an option from the menu: "))
            print()
            if 1 <= menu_option <= 9:
                return menu_option
            else:
                print("Invalid option. Please try again. You must choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# def validation_menu():

