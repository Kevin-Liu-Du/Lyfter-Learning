class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self._salary = value

    def promote(self, percentage):
        new_salary = self.salary * (1 + percentage)
        self._salary = new_salary
        print(f"Your new salary is {new_salary}.")


employee = Employee("Ana", 1000)

employee.promote(0.1)

print(employee.salary)