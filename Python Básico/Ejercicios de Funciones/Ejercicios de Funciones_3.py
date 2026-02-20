# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41

def sum_all_element_of_a_list(random_list):
    sum_1 = 0
    for numbers in random_list:
        sum_1 = sum_1 + numbers
        
    return sum_1


print(sum_all_element_of_a_list([4, 6, 2, 29]))