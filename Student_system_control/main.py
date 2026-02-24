import data
import actions
import menu

def main():
    student_list = []
    while True:
        menu.show_menu()
        option = menu.obtain_option()
        if option == 1:
            actions.add_student(student_list)
        elif option == 2:
            actions.show_all_students(student_list)
        elif option == 3:
            actions.show_top_3_students(student_list)
        elif option == 4:
            actions.show_average_grade_of_all_students(student_list)
        elif option == 5:
            data.export_CSV_file("students.csv", student_list, data.student_headers)
        elif option == 6:
            data.import_csv(student_list)
        elif option == 7:
            actions.delete_student(student_list)
        elif option == 8:
            actions.failed_students(student_list)
        elif option == 9:
            print("Exiting the program. Goodbye!")
            exit()

if __name__ == "__main__":
    main()

