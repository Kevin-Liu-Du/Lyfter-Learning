#Contar empleados por departamento

employees = [
    {"name": "Carlos", "department": "Ventas"},
    {"name": "Ana", "department": "TI"},
    {"name": "Luis", "department": "Ventas"},
    {"name": "Sofía", "department": "RRHH"},
]

result = {}

for item in employees:
    department = item["department"]
    if department in result:
        result[department] = result[department] + 1
    else:
        result[department] = 1

print(result)