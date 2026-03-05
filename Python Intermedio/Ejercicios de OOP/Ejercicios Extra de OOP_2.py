class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Muuuu"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow!"
    

dog = Dog("Firulais")
print(dog.speak())

cat = Cat("Michi")
print(cat.speak())

#this exercise is to show how to use inheritance and method overriding in Python.


