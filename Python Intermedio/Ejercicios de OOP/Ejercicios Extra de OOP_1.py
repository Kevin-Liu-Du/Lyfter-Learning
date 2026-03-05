class rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.height)
    

def validate_data():
    while True:
        try:
            base = float(input("Enter the base of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            if base <= 0 or height <= 0:
                print("Base and height must be positive numbers. Please try again.")
                continue
            return base, height
        except ValueError:
            print("Invalid input. Please enter numeric values for base and height.")

base, height = validate_data()
my_rectangle = rectangle(base, height)
print(f"The area of the rectangle is: {my_rectangle.get_area()}")
print(f"The perimeter of the rectangle is: {my_rectangle.perimeter()}")