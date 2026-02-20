#Create a program that asks the user for 3 numbers and displays the largest one.

counter = 0
list_grade = []
while (counter < 3):
    grade = int(input(f"Enter grade number {counter + 1}: "))
    list_grade.append(grade)
    counter += 1

if(list_grade[0] > list_grade[1] and list_grade[0] > list_grade[2]):
    print(f"The highest grade obtained is {list_grade[0]}.")
elif(list_grade[1] > list_grade[0] and list_grade[1] > list_grade[2]):
    print(f"The highest grade obtained is  {list_grade[1]}.")
else:
    print(f"The highest grade obtained is  {list_grade[2]}.")

#print(list_grade)