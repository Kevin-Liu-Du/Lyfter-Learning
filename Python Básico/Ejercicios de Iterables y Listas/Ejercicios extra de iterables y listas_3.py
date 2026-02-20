#Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list = [9, 4, 7, 1, 5]

'''
for numbers in range(0, len(my_list)):
    lowest = my_list[0]
    print(lowest)
    for number in my_list:
        if number < lowest:
            lowest = number
print(f"El manor valor es {lowest}")

'''

lowest = my_list[0]
for numbers in range(0, len(my_list)):
    for number in my_list:
        if number < lowest:
            lowest = number
print(f"El manor valor es {lowest}")