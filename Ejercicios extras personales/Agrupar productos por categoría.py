products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
    {"name": "Silla", "category": "Muebles", "price": 120},
]

result = {}

for item in products:
    category = item["category"]
    if category not in result:
        result[category] = []

    result[category].append(item)

print(result)