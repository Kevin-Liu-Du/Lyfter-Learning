products = [
    {"name": "TV", "category": "Electrónica", "price": 500},
    {"name": "Laptop", "category": "Electrónica", "price": 800},
    {"name": "Auriculares", "category": "Electrónica", "price": 150},
    {"name": "Sofá", "category": "Muebles", "price": 600},
    {"name": "Mesa", "category": "Muebles", "price": 300},
    {"name": "Cama", "category": "Muebles", "price": 900},
]

acumulado = {}

for productos_1 in products:
    categoria = productos_1["category"]
    monto = productos_1["price"]
    if categoria not in acumulado:
        acumulado[categoria] = monto
    else:
        acumulado[categoria] += monto

print(acumulado)

mayor_hasta_ahora = 0
for mayor in acumulado:
    mayor_1 = acumulado[mayor]
    if mayor_1 > mayor_hasta_ahora:
        mayor_hasta_ahora = mayor_1
        category = mayor
    else:
        mayor_hasta_ahora = mayor_hasta_ahora

print(f"La categoría más cara es {category} con un total de {mayor_hasta_ahora}")