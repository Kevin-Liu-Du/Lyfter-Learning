#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

random_list = [4, 3, 6, 1, 7]
#print(random_list)

first_deleted = random_list.pop(0)
last_deleted = random_list.pop(-1)

#print(first_deleted)
#print(last_deleted)
#print(random_list)

random_list.insert(0, last_deleted)
random_list.insert(len(random_list), first_deleted)
print(random_list)

#al hacer pop al primer elemento, la lista internamente se desplaza los elementos dentro de la lista, sin embargo al hacerle pop al ultimo elemento,, no hay desplazamiento
#con el insert, al insertarlo al inicio, hay un desplazamiento a la derecha, pero al insertarlo al final, no hay desplazamiento

x = random_list[0], random_list[-1] = random_list[0], random_list[-1]
print(random_list)
print(x)
