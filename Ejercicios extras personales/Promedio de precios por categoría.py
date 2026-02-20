products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Mouse", "category": "Electrónica", "price": 50},
    {"name": "Teclado", "category": "Electrónica", "price": 80},
    {"name": "Laptop", "category": "Electrónica", "price": 900},

    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Escritorio", "category": "Muebles", "price": 300},

    {"name": "Lámpara", "category": "Iluminación", "price": 60},
    {"name": "Foco LED", "category": "Iluminación", "price": 20},
]

result = {}
result_2 = {}

for item in products:
    category = item["category"]
    price = item["price"]
    if category not in result:
        result[category] = price
    else:
        result[category] += price

for productos in products:
    category = productos["category"]
    if category not in result_2:
        result_2[category] = 1
    else:
        result_2[category] = result_2[category] + 1

result_average = {}
for category in result:
    suma = result[category]
    amount = result_2[category]
    average = suma/amount
    result_average[category] = average

for average in result_average:
    print(f"El promedio de las ventas de {result_average[average]} es de {average}")

print(f"El promedio: {result_average}")    
print(f"La suma de precios por categorias: {result}")
print(f"La cantidad de categorias: {result_2}")