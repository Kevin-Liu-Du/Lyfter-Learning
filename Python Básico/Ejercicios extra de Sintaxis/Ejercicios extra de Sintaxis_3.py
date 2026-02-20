#Create an algorithm that asks the user for a number, and performs a sum of each number from 1 up to that entered number.
#Then display the result of the sum.

user = int(input("Enter a random number: "))

counter = 0
total = 0
while (counter < user):
    counter += 1
    total = total + counter

print(total)