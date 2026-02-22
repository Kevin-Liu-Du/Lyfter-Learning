#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total = {} #Aquí voy a guardar el total de precios por categoría

for item in products: #Voy a recorrer la lista products producto por producto, item es solo un producto, cada item equivale a un diccionario con informacion del producto
        category = item["category"] #Extrae la categoría del producto actual, es un string
        price = item["price"] #Extrae el precio del producto actual, son numeros
        if category in total: #Ya existe esta categoría como clave en el diccionario total
            total[category] = total[category] + price
        else:
            total[category] = price

print(total)

'''
condiciones
caso 1: la categoría YA existe
ejemplo
total = {"Electrónica": 200}
Entonces se ejecuta:
total[category] = total[category] + price
Suma el precio del producto actual al total que ya tenía esa categoría
200 + 50 = 250

caso 2: la categoría NO existe todavía
total = {}
Entonces se ejecuta:
total[category] = price
Crea la categoría y guarda el precio del primer producto como valor inicial
"Electrónica": 200
'''

