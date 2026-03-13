class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Woof! My name is {self.name} and I am {self.age} years old.")

dog1 = Dog("Firulais", 5) #creating an instance of the Dog class with the name "Firulais" and age 5
dog1.bark()