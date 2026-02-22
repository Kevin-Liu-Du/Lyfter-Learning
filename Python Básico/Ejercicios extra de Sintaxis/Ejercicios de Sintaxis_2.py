#Create a program that asks the user for their first name, last name, and age, and displays whether they are a baby, child,
#preteen, teenager, young adult, adult, or senior citizen.

name = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age <= 0:
    print("Error: the age must be greater than 0.")
elif age <= 2:
    print(f'{name} {lastname}, {age} years old is a baby.')
elif age <= 9:
    print(f'{name} {lastname}, {age} years old is a child.')
elif age <= 12:
    print(f'{name} {lastname}, {age} years old is a preteen.')
elif age <= 17:
    print(f'{name} {lastname}, {age} years old is a teenager')
elif age <= 29:
    print(f'{name} {lastname}, {age} years old is a young adult')
elif age <= 59:
    print(f'{name} {lastname}, {age} years old is an adult')
else:
    print(f'{name} {lastname}, {age} years old is a senior citizen')