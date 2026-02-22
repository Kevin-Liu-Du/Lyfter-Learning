#Given a student's n grades, calculate:
#How many grades are passing (greater than 70).
#How many grades are failing (less than 70).
#The average grade, the average of passing grades, and the average of failing grades.

amount_grade = int(input("Enter the amount of grades: "))
counter = 0
counter_approved = 0
counter_unapproved = 0
grade_list = []
approved_list = []
unapproved_list = []
while (counter < amount_grade):
    grades = int((input(f"Enter grade number {counter + 1}: ")))
    counter += 1
    grade_list.append(grades)
    if (grades >= 70):
        counter_approved += 1
        approved_list.append(grades)
    else:
        counter_unapproved +=1
        unapproved_list.append(grades)

average = sum(grade_list)/amount_grade
if (counter_approved > 0):
    average_approved = sum(approved_list)/counter_approved
    print(f"The average of approved grades is {average_approved}.")

    print(f"The number of approved grades is {counter_approved}, which are: ")
    for grade in approved_list:
        print(grade, end = " ")
else:
    print("There is no average or number of those who passed because there are no grades.")

if(counter_unapproved > 0):
    average_unapproved = sum(unapproved_list)/counter_unapproved
    print(f"The average of failing grades is {average_unapproved}.")
    print(f"The number of failing grades is {counter_unapproved}, which are: ")
    for grade in unapproved_list:
        print(grade, end = " ")
    
else:
    print(" ")
    print("There is no average or number of failures because there are no grades")


print(f"The average grade is  {average}.")
