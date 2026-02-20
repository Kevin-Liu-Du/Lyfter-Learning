#Create a program with a secret number from 1 to 10. The program should not close until the user guesses the number.
#You must research how to generate a different random number each time the program runs.

import random
secret_number = random.randint(1, 10)
print(secret_number)

user = int(input("Enter a random number from 1 to 10: "))


while (user != secret_number):
    if user < 1 or user > 10:
        print("Invalid number, you must enter a number from 1 - 10.")
    else:
        print("Incorrect number, please try again.")

    user = int(input("Enter another number: "))

print("correct number")