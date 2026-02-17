#Crea una función total_por_categoria(productos) donde productos es una lista de diccionarios con esta
# [
#   {"nombre": "Laptop", "categoria": "Tecnología", "precio": 1200},
#   {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25},
#   {"nombre": "Silla", "categoria": "Muebles", "precio": 150}
# ]

def total_per_category(products):
    for items in products:
        #print(items)
        category = items["categoria"]
        price = items["precio"]
        return category, price

def sum_total():
    category = total_per_category(products_list)
    price = total_per_category(products_list)
    total_list = {}
    if category in total_list:
        total_list[category] = total_list[category] + price
    else:
        total_list[category] = price

    return total_list


products_list = [
    {"nombre": "Laptop", "categoria": "Tecnología", "precio": 1200},
    {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25},
    {"nombre": "Silla", "categoria": "Muebles", "precio": 150}
]

print(sum_total())