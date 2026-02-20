'''
contador = 0

while contador < 3:
    print("Iteración del while:", contador)

    for i in range(5):
        print("  for:", i)

    contador += 1
    

filas = [1, 2, 3]
columnas = ['A', 'B']

for f in filas:
    for c in columnas:
        print(f, c)



my_list = [3, 6, 0, -2, 4]
for numbers in range(0, len(my_list)):
    print(numbers)

for index, numbers in enumerate(my_list):
    numbers = my_list[index]
    print(index)

'''

list_x = ["hola", "si"]
print(list_x[0][1])
