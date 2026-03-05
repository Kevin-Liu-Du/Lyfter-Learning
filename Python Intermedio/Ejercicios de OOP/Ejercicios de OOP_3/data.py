import csv
from actions import Student 

student_headers = (
    "name",
    "class_number",
    "spanish",
    "english",
    "social_studies",
    "science"
)

def export_CSV_file(file_path, data, headers):
    if not data:
        print("No students to export.")
        return
    else:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            dict_data = [student.to_dict() for student in data]
            writer.writerows(dict_data)
            print(f"Data exported successfully to {file_path}.")

def import_csv(student_list):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file) #with dictreader, each row of the CSV file is read as a dictionary, where the keys are the column headers and the values are the corresponding data for each student.
            #dictreader convert to string, so we need to convert the grade values to floats for calculations and comparisons in the program.
            warning_message = "Warning: Importing data will overwrite the current student list. Do you want to continue? (yes/no): "
            while True:
                user_input = input(warning_message).strip().lower()
                if user_input == "yes":
                    student_list.clear() #It clears the current student list before importing the new data, ensuring that the imported data replaces the existing data.
                    for row in reader:
                        student_instance = Student(
                            name=row["name"],
                            class_number=row["class_number"],
                            spanish=float(row["spanish"]),
                            english=float(row["english"]),
                            social_studies=float(row["social_studies"]),
                            science=float(row["science"])
                        )
                        student_list.append(student_instance)
                    print("Data imported successfully.")
                    break
                elif user_input == "no":
                    print("Import cancelled.")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
    except FileNotFoundError:
        print("No exported file found.")