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

def add_products(random_list):
    new_product = {}
    name = input("Enter the product name:")
    new_product["nombre"] = name

    stock = float(input("Enter the stock quantity: "))
    new_product["stock"] = stock

    price = float(input("Enter the product price: "))
    new_product["precio"] = price

    random_list.append(new_product)

    return random_list


print(add_products(inventario))

def calculate(random_list):
    ask_product = input("Enter the product you want to calculate: ")

    encontrado = False   # ← asumimos que NO existe

    for each_dictionary in random_list:
        product_name = each_dictionary["nombre"]

        if ask_product == product_name:
            value = each_dictionary["stock"] * each_dictionary["precio"]
            print(value)
            encontrado = True   # ← ahora sabemos que SÍ existe
            break

    if not encontrado:
        print("Product not found in inventory")

calculate(inventario)

