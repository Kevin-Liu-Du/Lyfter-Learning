class Engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car():
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Horsepower: {self.engine.horsepower}")

engine1 = Engine(150)
car1 = Car("Toyota", engine1)
car1.show_specs()