sales = [
    {"email": "juan@gmail.com", "amount": 120},
    {"email": "ana@gmail.com", "amount": 80},
    {"email": "juan@gmail.com", "amount": 60},
    {"email": "carlos@yahoo.com", "amount": 200},
    {"email": "ana@gmail.com", "amount": 40},
    {"email": "maria@outlook.com", "amount": 150},
    {"email": "juan@gmail.com", "amount": 30},
    {"email": "carlos@yahoo.com", "amount": 100},
    {"email": "maria@outlook.com", "amount": 50},
    {"email": "ana@gmail.com", "amount": 70},
]

result = {}

for people in sales:
    email = people["email"]
    amount = people["amount"]

    if email not in result:
        result[email] = amount
    else:
        result[email] += amount

print(result)