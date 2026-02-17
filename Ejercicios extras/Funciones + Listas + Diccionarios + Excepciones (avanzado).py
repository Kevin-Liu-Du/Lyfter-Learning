inventario = [
    {
        "nombre": "Teclado",
        "stock": 10,
        "precio": 35.0
    },
    {
        "nombre": "Mouse",
        "stock": 25,
        "precio": 15.5
    },
    {
        "nombre": "Monitor",
        "stock": 5,
        "precio": 220.99
    },
    {
        "nombre": "Laptop",
        "stock": 3,
        "precio": 1200.0
    }
]

def menu():
    menu = {
        1: "Add products",
        2: "Calculate",
        3: "Inventory Result",
        4: "Exit"
    }

    for number, options in menu.items():
        print(f"{number}. {options}")

    return menu

def read_menu_option(): 
    while True:
        try:
            options = int(input("Select an option from the menu: "))
            return options
        except ValueError:
                print("Error, you must enter a valid number from the menu.")

def validation_number(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("The value must be greater than 0.")
            else:
                return value
        except ValueError:
            print("You must enter a valid number.")


def add_products(inventory_list):
    new_product = {}
    name = input("Enter de product name: ")
    stock = validation_number("Enter de amount of stock: ")
    price = validation_number("Enter the price: ")
    new_product["nombre"]  = name
    new_product["stock"] = stock
    new_product["precio"] = price

    inventory_list.append(new_product)





def main():
    returned_menu = menu()
    options = returned_menu.keys()

    selected_options = 0

    while selected_options != 4:
        selected_options = read_menu_option()
        if selected_options not in options:
            print("Number does not correspond to the menu.")
            continue

        if selected_options == 1:
            add_products(inventario)

        #if selected_options == 2:    

        if selected_options == 3:
            print(inventario)


if __name__ == "__main__":
    main()

#primera version

