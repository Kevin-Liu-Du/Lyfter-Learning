#Cree un programa que verifique si todos los elementos de una lista son positivos

my_list = [3, 6, 0, -2, 4]

for numbers in range(0, len(my_list)):
    if my_list[numbers] <= 0:
        print("There is at least one negative number or zero.")
    else:
        print("There is no negative or zero number.")
        break

#for numbers in range(0, len(my_list)):
#    if numbers <= 0: #estaba evaluando solo el indice de los elementos
#        print("There is at least one negative number or zero.")