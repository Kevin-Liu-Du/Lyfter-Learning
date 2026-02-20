def menu():
    options = {
        1: "Add products",
        2: "Calculate",
        3: "Inventory Result",
        4: "Exit"
    }

    for number, option in options.items():
        print(f"{number}. {option}")

    menu_option = int(input("Select a menu option: "))
    return menu_option


def add_products(inventory):
    new_product = {}

    name = input("Enter the product name: ")
    new_product["nombre"] = name

    stock = float(input("Enter the stock quantity: "))
    new_product["stock"] = stock

    price = float(input("Enter the product price: "))
    new_product["precio"] = price

    inventory.append(new_product)


def calculate(inventory):
    ask_product = input("Enter the product you want to calculate: ")

    found = False

    for product in inventory:
        if product["nombre"] == ask_product:
            value = product["stock"] * product["precio"]
            print(f"Total value: {value}")
            found = True
            break

    if not found:
        print("Product not found in inventory")


def inventory_result(inventory):
    if not inventory:
        print("Inventory is empty")
        return

    print("\nCurrent inventory:")
    for product in inventory:
        print(
            f"Name: {product['nombre']}, "
            f"Stock: {product['stock']}, "
            f"Price: {product['precio']}"
        )


def main():
    inventory = []

    while True:
        option = menu()

        if option == 1:
            add_products(inventory)
        elif option == 2:
            calculate(inventory)
        elif option == 3:
            inventory_result(inventory)
        elif option == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid option")


main()
