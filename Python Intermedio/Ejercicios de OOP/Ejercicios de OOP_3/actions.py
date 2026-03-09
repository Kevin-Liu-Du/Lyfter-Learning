from validations import validate_integer, validate_name, validate_grade, validate_section

class Student:
    def __init__(self, name, class_number, spanish, english, social_studies, science):
        self.name = name
        self.class_number = class_number
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def to_dict(self):
        return {
            "name": self.name,
            "class_number": self.class_number,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science
        }
    
    def average(self):
        return (
            self.spanish
            + self.english
            + self.social_studies
            + self.science
        ) / 4

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

        student_list.append(Student(name, section, spanish, english, social_studies, science))



def validate_student_exists(student_list, name, section):
    for student in student_list:
        if student.name.lower() == name.lower() and student.class_number.lower() == section.lower():
            return True
    return False
    


def calculate_top_3_students(student_list):
    sorted_students = sorted(
        student_list,
        key=lambda student: student.average(),
        reverse=True
    )
    top_3 = sorted_students[:3]
    return [(student, student.average()) for student in top_3]



def print_top_3_students(student_list):
    top_students = calculate_top_3_students(student_list)

    if not top_students:
        print("No students to show.")
        return

    print("Top 3 Students:")

    for index, (student, average) in enumerate(top_students, start=1):
        print(f"{index}. {student.name} - {average:.2f}")



def show_all_students(student_list):
    if not student_list:
        print("No students to show.")
    else:
        sorted_students = sorted(student_list, key=lambda student: student.name)

        print("All students sorted alphabetically:\n")

        for index, student in enumerate(sorted_students, start=1):
            print(
                f"--- Student #{index} ---\n"
                f"Student: {student.name}\n"
                f"Class number: {student.class_number}\n"
                f"Spanish: {student.spanish}\n"
                f"English: {student.english}\n"
                f"Social Studies: {student.social_studies}\n"
                f"Science: {student.science}\n"
                "------------------------"
            )

        print()

    total_students = len(student_list)
    print(f"Total number of students: {total_students}")



def show_average_grade_of_all_students(student_list):
    if not student_list:
        print("No students to calculate average.")
    else:
        average_list = [student.average() for student in student_list]
        all_average = sum(average_list) / len(average_list)
        print(f"The average grade of all students is: {all_average:.2f}")



def delete_student(student_list):
    if not student_list:
        print("No students to delete.")
    else:
        name_to_delete = validate_name("Enter the name of the student you want to delete: ")
        class_number_to_delete = validate_section("Enter the class number of the student you want to delete: ")

        for student in student_list:
            if (student.name.lower() == name_to_delete.lower() and
                student.class_number.lower() == class_number_to_delete.lower()):

                confirmation = input(
                    f"Are you sure you want to delete student '{name_to_delete}' "
                    f"with class number '{class_number_to_delete}'? (yes/no): "
                )

                if confirmation.lower() == "yes":
                    student_list.remove(student)
                    print(f"Student '{name_to_delete}' has been deleted.")
                break
        else:
            print(f"No student found with the name '{name_to_delete}' "
                    f"and class number '{class_number_to_delete}'.")



def failed_students(student_list):
    if not student_list:
        print("No failed students to show.")
    else:
        for student in student_list:
            failed_materials = []

            if student.spanish < 60:
                failed_materials.append(f"\n- Spanish: {student.spanish}")

            if student.english < 60:
                failed_materials.append(f"\n- English: {student.english}")

            if student.social_studies < 60:
                failed_materials.append(f"\n- Social Studies: {student.social_studies}")

            if student.science < 60:
                failed_materials.append(f"\n- Science: {student.science}")

            if failed_materials:
                print("----- Failed Student -----")
                print(
                    f"{student.name} from class {student.class_number} "
                    f"has failed the following subjects:"
                    f"{''.join(failed_materials)}\n"
                )

    print()
    total_failed_students = len([student for student in student_list if student.average() < 60])
    print(f"Total number of failed students: {total_failed_students}")  
