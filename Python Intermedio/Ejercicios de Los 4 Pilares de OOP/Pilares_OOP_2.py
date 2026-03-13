from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, name): 
        self.radius = radius 
        self.name = name
    
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print(f"The perimeter of the shape {self.name} is {perimeter:.2f}.")


    def calculate_area (self): 
        area = 3.14 * self.radius ** 2
        print(f"The area of the shape {self.name} is {area}.")

class Square(Shape):
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side_length
        print(f"The perimeter of the shape {self.name} is {perimeter}.")

    def calculate_area(self):
        area = self.side_length * 2
        print(f"The area of the shape {self.name} is {area}.")


class Rectangle(Shape):
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

    def calculate_perimeter(self):
        perimeter = (self.width + self.height) * 2
        print(f"The perimeter of the shape {self.name} is {perimeter}.")


    def calculate_area(self):
        area = self.width * self.height
        print(f"The area of the shape {self.name} is {area}.")



circle = Circle(5, "Circle")
square = Square(4, "Square")
rectangle = Rectangle(3, 6, "Rectangle")

circle.calculate_area()
circle.calculate_perimeter()
print()
square.calculate_area()
square.calculate_perimeter()
print()
rectangle.calculate_perimeter()
rectangle.calculate_area()