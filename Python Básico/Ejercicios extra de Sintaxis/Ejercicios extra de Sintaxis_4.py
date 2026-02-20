#Create a flowchart that asks the user for 3 numbers. If one of those numbers is 30,
# or if the sum of the 3 numbers is 30, display “Correct”. Otherwise, display “Incorrect”.

counter = 0
number_list = []
while (counter < 3):
    user = int(input(f"Enter the {counter + 1} number: "))
    number_list.append(user)
    counter += 1

if(sum(number_list) == 30):
    print("Correct")
elif (number_list[0] == 30 or number_list[1] == 30 or number_list[2] == 30):
    print("Correct")
else:
    print("Incorrect")