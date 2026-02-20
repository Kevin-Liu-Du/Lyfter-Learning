students = [
    {"name": "Juan", "grade": 85},
    {"name": "María", "grade": 62},
    {"name": "Pedro", "grade": 70},
    {"name": "Ana", "grade": 90},
]

result = {}

for notas in students:
    grades = notas["grade"]

    if "Aprobado" not in result:
        result["Aprobado"] = []
    
    if "Reprobado" not in result:
        result["Reprobado"] = []

    if grades >= 70:
        result["Aprobado"].append(notas)
    else:
        result["Reprobado"].append(notas)
    
print(result)