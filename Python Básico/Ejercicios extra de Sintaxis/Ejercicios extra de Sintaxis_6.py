#Custom multiplication table
#Ask the user for a number from 1 to 10
#Display their multiplication table from 1 to 12


number = int(input("Enter a number from 1 to 10: "))
counter = 1
while (counter <= 12):
    multiplication = number * counter
    print(f"{number} * {counter} = {multiplication}")
    counter += 1