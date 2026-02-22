#Dada una lista de productos con categoría, crea un diccionario que indique cuántos productos hay por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica"},
    {"name": "Teclado", "category": "Electrónica"},
    {"name": "Silla", "category": "Muebles"},
    {"name": "Mesa", "category": "Muebles"},
    {"name": "Mouse", "category": "Electrónica"},
]

result = {}

for item in products:
    category = item["category"] # = Primera vuelta = Electronica es un string
    #print(category)
    if category in result: # si esa categoria existe en resultado
        result[category] = result[category] + 1 # categoria va ser igual a esa categoria pero sumandole 1
    else: # de lo contrario
        result[category] =  1#hay que crear la categoria y asignarle un 1

print(result)