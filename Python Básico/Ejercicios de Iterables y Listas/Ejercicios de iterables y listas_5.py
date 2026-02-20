#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

user_list = []


for numbers in range(0, 10):
    numbers = int(input("Enter a number: "))
    user_list.append(numbers)

highest = user_list[0]

for number in user_list:
    if number > highest:
        highest = number



print(f"{user_list}. The highest number is {highest}")