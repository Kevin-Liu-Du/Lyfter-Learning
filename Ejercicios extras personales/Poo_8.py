class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine Started")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        self.engine.start()

    def car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Horsepower: {engine.horsepower}")


# engine = Engine(150)
# engine.start()


engine = Engine(200)

car = Car("Toyota", engine)

car.start_car()

car.car_info()