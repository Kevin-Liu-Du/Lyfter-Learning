class Student():
    def __init__(self, name, spanish, english, science):
        self.name = name
        self.spanish = spanish
        self.english = english
        self.science = science
        student_list = []
    
    def average(self):
        print(self.spanish + self.english + self.science) / 3
    
    def sort_student(self):
        sorted_list = sorted(self.student_list, reverse=True)
        print(sorted_list)

    def top_3(self):
        top_3 = self.sorted_list[:3]
        print("Top Students:")
        for grade in top_3:
            print(f"{self.name}: {grade}")

student1 = Student("Kevin", 90, 85, 88)

student1.average()