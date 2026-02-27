from validations import validate_integer, validate_name, validate_grade, validate_section


def add_student(student_list):
    amount = validate_integer("How many students do you want to add? ")
    print()
    for _ in range(amount):
        while True:
            name = validate_name("Enter the student's name: ")
            section = validate_section("Enter the student's class number: ")
            if validate_student_exists(student_list, name, section):
                print(f"A student with the name '{name}' and class number '{section}' already exists. Please enter a different name or class number.")
            else:
                break

        spanish = validate_grade("Enter Spanish grade: ")
        english = validate_grade("Enter English grade: ")
        social_studies = validate_grade("Enter Social Studies grade: ")
        science = validate_grade("Enter Science grade: ")
        print(f"\n student '{name}' added successfully.\n")

        student_list.append({
            "name": name,
            "class_number": section,
            "spanish": spanish,
            "english": english,
            "social_studies": social_studies,
            "science": science
        })



def validate_student_exists(student_list, name, section):
    for student in student_list:
        if student["name"].lower() == name.lower() and student["class_number"].lower() == section.lower():
            return True
    return False
    



def calculate_average(student): #return a float value that represents the average grade of a student
        return (
            student["spanish"]
            + student["english"]
            + student["social_studies"]
            + student["science"]
        ) / 4



def calculate_top_3_students(student_list):
    sorted_students = sorted(
        student_list,
        key=calculate_average,
        reverse=True
    )

    top_3 = sorted_students[:3]

    return [(student, calculate_average(student)) for student in top_3]



def print_top_3_students(student_list):
    top_students = calculate_top_3_students(student_list)

    if not top_students:
        print("No students to show.")
        return

    print("Top 3 Students:")

    for index, (student, average) in enumerate(top_students, start=1):
        print(f"{index}. {student['name']} - {average:.2f}")



def show_all_students(student_list):
    if student_list == []:
        print("No students to show.")
    else:
        sorted_students = sorted(student_list, key=lambda student: student["name"])
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

        total_students = len(student_list)
        print(f"Total number of students: {total_students}")



def show_average_grade_of_all_students(student_list):
    if student_list == []:
        print("No students to calculate average.")
    else:
        average_list = [calculate_average(student) for student in student_list]
        all_average = sum(average_list) / len(average_list) #floats cannot be iterated
        print(f"The average grade of all students is: {all_average:.2f}")



def delete_student(student_list):
    if student_list == []:
        print("No students to delete.")
    else:
        name_to_delete = validate_name("Enter the name of the student you want to delete: ")
        class_number_to_delete = validate_section("Enter the class number of the student you want to delete: ")
        for student in student_list:
            if student["name"].lower() == name_to_delete.lower() and student["class_number"].lower() == class_number_to_delete.lower():
                confirmation = input(f"Are you sure you want to delete student '{name_to_delete}' with class number '{class_number_to_delete}'? (yes/no): ")
                if confirmation.lower() == "yes":
                    student_list.remove(student)
                    print(f"Student '{name_to_delete}' has been deleted.")
                    break
        else:
            print(f"No student found with the name '{name_to_delete}' and class number '{class_number_to_delete}'.")



def failed_students(student_list):
    if student_list == []:
        print("No failed students to show.")
    else:
        for students in student_list:
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
