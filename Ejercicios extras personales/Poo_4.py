class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self, student):
        print(f"Name: {student.name}, Grade: {student.grade}")


student1 = Student("Alice", 85) #this is an instance/object
student2 = Student("Bob", 90)
students = [student1, student2]
for student in students:
    student.show_info(student)
