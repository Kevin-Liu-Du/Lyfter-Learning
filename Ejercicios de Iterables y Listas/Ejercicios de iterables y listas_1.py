#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy', 'hola']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util',]
#print(f"La longitud es de {len(second_list)}")


counter = 0
while counter < len(first_list) and counter < len(second_list):
    print(first_list[counter] + " " + second_list[counter])
    counter += 1

for index in range(0, min(len(second_list), len(first_list))):
    combination = first_list[index] + " " + second_list[index]
    print(combination)