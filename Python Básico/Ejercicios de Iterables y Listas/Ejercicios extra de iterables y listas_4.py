#Cree un programa que reciba una lista de números y calcule el promedio de los valores, 
#luego cree una nueva lista con solo los valores mayores al promedio

'''
user_list = []
new_list = []

amount = int(input("Enter the number of numbers you want for the list: "))
for numbers in range(0, amount):
    numbers = int(input("Enter a number: "))
    user_list.append(numbers)

first_highest = user_list[0]
for number in user_list:
    if number > first_highest:
        first_highest = number
        
new_list.append(first_highest)

second_highest = user_list[1]
for number in user_list:
    if number < first_highest and number > user_list[1]:
        second_highest = number

new_list.append(second_highest)

#print(user_list)
average = sum(user_list)/amount
print(f"The average is {average}")

print(f"The new list is: {new_list}")
'''

user_list = []
new_list = []

amount = int(input("Enter the number of numbers you want for the list: "))
for numbers in range(0, amount):
    numbers = int(input("Enter a number: "))
    user_list.append(numbers)

#print(user_list)
average = sum(user_list)/amount
print(f"The average is {average}")

for numbers in user_list:
    if numbers > average:
        new_list.append(numbers)

print(user_list)
print(new_list)