sales = [
    {"date": "2024-01-01", "amount": 150},
    {"date": "2024-01-02", "amount": 200},
    {"date": "2024-01-01", "amount": 100},
    {"date": "2024-01-03", "amount": 50},
    {"date": "2024-01-02", "amount": 75},
]

result = {}

for ventas in sales:
    fecha = ventas["date"]
    monto = ventas["amount"]
    if fecha not in result:
        result[fecha] = monto
    else:
        result[fecha] += monto
    
print(result)