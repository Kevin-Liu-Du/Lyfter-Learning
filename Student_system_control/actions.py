from validations import validate_integer, validate_name, validate_grade, validate_section

import storage

def add_student():
    amount = validate_integer("How many students do you want to add? ")
    print()
    for _ in range(amount):
        while True:
            name = validate_name("Enter the student's name: ")
            
            if any(name.lower() == student["name"].lower() for student in storage.student_list):
                print("This student already exists. Please enter a different name.")
                continue #It will continue asking until the name does not exist, in other words, it returns to the beginning of the while loop to ask for another name.

            break  #exits the while loop because the name is valid and is not repeated

        section = validate_section("Enter the student's class number: ")
        spanish = validate_grade("Enter Spanish grade: ")
        english = validate_grade("Enter English grade: ")
        social_studies = validate_grade("Enter Social Studies grade: ")
        science = validate_grade("Enter Science grade: ")
        print(f"\n student '{name}' added successfully.\n")

        storage.student_list.append({
            "name": name,
            "class_number": section,
            "spanish": spanish,
            "english": english,
            "social_studies": social_studies,
            "science": science
        })


    #print(storage.student_list)

def average_grade_of_each_student():
    averages = []
    for student in storage.student_list:
        grade = (student["spanish"] + student["english"] + student["social_studies"] + student["science"]) / 4
        averages.append(grade)
    return averages



def show_all_students():
    if storage.student_list == []:
        print("No students to show.")
    else:
        sorted_students = sorted(storage.student_list, key=lambda student: student["name"])
        print(f"All students sorted alphabetically:\n")
        for index, student in enumerate(sorted_students, start=1):
            print(
                f"------Student #{index}------\n"
                f"Student: {student['name']}\n"
                f"Class number: {student['class_number']}\n"
                f"Spanish: {student['spanish']}\n"
                f"English: {student['english']}\n"
                f"Social Studies: {student['social_studies']}\n"
                f"Science: {student['science']}\n"
                "-----------------------"
            )
            print()

        total_students = len(storage.student_list)
        print(f"Total number of students: {total_students}")

def show_top_3_students():
    if storage.student_list == []:
        print("No students to show.")
    else:
        sorted_students = sorted(storage.student_list, key=lambda student: (student["spanish"] + student["english"] + student["social_studies"] + student["science"]) / 4, reverse=True) 
        #key tells sorted how to sort the students, in this case using a lambda function that calculates the average of each student's grades.
        #reverse=True tells sorted to sort from highest to lowest, meaning that students with the highest averages will appear first in the sorted list.
        #sorted_students is the list of students sorted from highest to lowest according to their grade point average.

        top_3_students = sorted_students[:3]
        #[:3] takes the first 3 students from the sorted list, which are those with the highest averages since it was sorted from highest to lowest using reverse=True. Without considering the element at index 3, that is, the fourth element in the list.
        print("Top 3 Students:")
        #that start=1 makes the index start at 1 instead of 0, which is useful for displaying students as “1. Student name” instead of “0. Student name”.
        for index, student in enumerate(top_3_students, start=1):
            average = (
                student["spanish"]
                + student["english"]
                + student["social_studies"]
                + student["science"]
            ) / 4

            print(f"{index}. {student['name']} - {average:.2f}")


def show_average_grade_of_all_students():
    if storage.student_list == []:
        print("No students to calculate average.")
    else:
        average_list = average_grade_of_each_student()
        all_average = sum(average_list) / len(average_list) #floats cannot be iterated
        print(f"The average grade of all students is: {all_average:.2f}")

def delete_student():
    if storage.student_list == []:
        print("No students to delete.")
    else:
        name_to_delete = validate_name("Enter the name of the student you want to delete: ")
        class_number_to_delete = validate_section("Enter the class number of the student you want to delete: ")
        for student in storage.student_list:
            if student["name"].lower() == name_to_delete.lower() and student["class_number"].lower() == class_number_to_delete.lower():
                confirmation = input(f"Are you sure you want to delete student '{name_to_delete}' with class number '{class_number_to_delete}'? (yes/no): ")
                if confirmation.lower() == "yes":
                    storage.student_list.remove(student)
                    print(f"Student '{name_to_delete}' has been deleted.")
                    break
        else:
            print(f"No student found with the name '{name_to_delete}' and class number '{class_number_to_delete}'.")


def failed_students():
    if storage.student_list == []:
        print("No students to show.")
    else:
        for students in storage.student_list:
            spanish = students["spanish"]
            english = students["english"]
            social_studies = students["social_studies"]
            science = students["science"]
            name = students["name"]
            section = students["class_number"]
            failed_materials = []
            if spanish < 60:
                failed_materials.append(f"\n- Spanish: {spanish}")
            if english < 60: #do not use elif, since only the first if would be evaluated and if it is false, the second if would not be evaluated. 
                #which is not correct because a student could have failed both subjects, 
                #Therefore, both if statements must be evaluated independently to verify whether the student has failed any of the subjects.
                failed_materials.append(f"\n- English: {english}") 
            if social_studies < 60:
                failed_materials.append(f"\n- Social Studies: {social_studies}")
            if science < 60:
                failed_materials.append(f"\n- Science: {science}")
            if failed_materials:
                print(f"------Failed Student:------")
                print(f"{name} from class {section} has failed the following subjects: {''.join(failed_materials)}\n")
