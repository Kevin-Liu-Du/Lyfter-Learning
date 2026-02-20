#Cree un programa que elimine todos los números impares de una lista.
#Ejemplos:
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numero impar = n mod 2 != 0 


for index in range(len(random_list)-1, -1, -1):
    #print(index)
    #print(random_list[index])
    if (random_list[index] % 2 != 0): #odd
        random_list.pop(index)

print(random_list)