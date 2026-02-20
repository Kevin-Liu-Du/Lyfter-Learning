import csv
import storage

student_headers = (
    "name",
    "class_number",
    "spanish",
    "english",
    "social_studies",
    "science"
)

def export_CSV_file(file_path, data, headers):
    if storage.student_list == []:
        print("No students to export.")
    else: 
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers) 
            writer.writeheader()
            writer.writerows(data)
            print(f"Data exported successfully to {file_path}.")



def import_csv():
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file) #with dictreader, each row of the CSV file is read as a dictionary, where the keys are the column headers and the values are the corresponding data for each student.
            #dictreader convert to string, so we need to convert the grade values to floats for calculations and comparisons in the program.
            warning_message = "Warning: Importing data will overwrite the current student list. Do you want to continue? (yes/no): "
            while True:
                user_input = input(warning_message).strip().lower()
                if user_input == "yes":
                    storage.student_list.clear() #It clears the current student list before importing the new data, ensuring that the imported data replaces the existing data.
                    for row in reader:
                        try:
                            row["spanish"] = float(row["spanish"]) #It converts the string values from the CSV file into floats, which is necessary for the grade data to be used correctly in calculations and comparisons within the program.
                            row["english"] = float(row["english"])
                            row["social_studies"] = float(row["social_studies"])
                            row["science"] = float(row["science"])
                        except (ValueError, TypeError):
                            print("Invalid data format in CSV.")
                            #print(reader.fieldnames) #It prints the field names of the CSV file, which can help identify any issues with the data format or structure in the CSV file.
                            #print(row)
                            return
                        storage.student_list.append(row)
                    print("Data imported successfully.")
                    break
                elif user_input == "no":
                    print("Import cancelled.")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
    except FileNotFoundError:
        print("No exported file found.")

