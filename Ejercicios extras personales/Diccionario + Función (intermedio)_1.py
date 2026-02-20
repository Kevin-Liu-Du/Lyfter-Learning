#Crea una función total_por_categoria(productos) donde productos es una lista de diccionarios con esta
# [
#   {"nombre": "Laptop", "categoria": "Tecnología", "precio": 1200},
#   {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25},
#   {"nombre": "Silla", "categoria": "Muebles", "precio": 150}
# ]

def main(random_list):
    result = {}
    for element in random_list:
        category = element["categoria"]
        price = element["precio"]

        if category in result:
            result[category] = result[category] + price
        else:
            result[category] = price

    return result

random_list = [
    {"nombre": "Laptop", "categoria": "Tecnología", "precio": 1200},
    {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25},
    {"nombre": "Silla", "categoria": "Muebles", "precio": 150}
]

if __name__ == "__main__":
    print(main(random_list))