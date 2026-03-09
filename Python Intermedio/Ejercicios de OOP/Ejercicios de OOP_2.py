class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.passengers = []
        self.max_passengers = max_passengers

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} boarded the bus.")
        else:
            print(f"The passenger {passenger.name} cannot board the bus. The bus is full.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger.name} left the bus.")
        else:
            print(f"The passenger {passenger} is not on the bus.")

bus = Bus(3)

person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
person4 = Person("David")

bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4)


bus.remove_passenger(person1)
bus.remove_passenger("Eve")