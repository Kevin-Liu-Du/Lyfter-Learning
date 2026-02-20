emails = [
    "juan@gmail.com",
    "ana@yahoo.com",
    "carlos@gmail.com",
    "sofia@outlook.com",
]

result = {}

for correo in emails:
    separate = correo.split("@")
    domain = separate[1]
    if domain not in result:
        result[domain] = []
    
    result[domain].append(correo)

print(result)