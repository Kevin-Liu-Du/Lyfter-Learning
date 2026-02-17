# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
# Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
# Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

#Un número es primo si, aparte de dividirse por 1 y por sí mismo,
#todas las demás divisiones dejan residuo. 

def found_prime_numbers(list_number):
    if list_number <= 1:
        return False
    for number in range(2, list_number):
        if list_number % number  == 0:
            return False
    return True

def prime_number_list(random_list):
    result_list = []
    for numbers in random_list:
        if found_prime_numbers(numbers) == True:
            result_list.append(numbers)
        
    return result_list

print(prime_number_list([1, 4, 6, 7, 13, 9, 67]))
