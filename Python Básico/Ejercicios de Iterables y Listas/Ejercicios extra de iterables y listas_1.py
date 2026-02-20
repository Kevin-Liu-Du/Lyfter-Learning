#Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar

user_list = []

amount = int(input("Enter the number of numbers you want for the list: "))

for numbers in range(0, amount):
    numbers = int(input("Enter a number: "))
    user_list.append(numbers)

search_number = int(input("Enter the number you are looking for: "))

counter_number = 0
for number in user_list:
    if (number == search_number):
        counter_number += 1

print(f"The number {search_number} appears {counter_number} times.")


