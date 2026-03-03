class Bus:
    def __init__(self, max_passengers):
        self.passengers = []
        self.max_passengers = max_passengers

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger} boarded the bus.")
        else:
            print(f"The passenger {passenger} cannot board the bus. The bus is full.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger} left the bus.")
        else:
            print(f"The passenger {passenger} is not on the bus.")

bus = Bus(3)
bus.add_passenger("Alice")
bus.add_passenger("Bob")
bus.add_passenger("Charlie")
bus.add_passenger("David")


bus.remove_passenger("Alice")
bus.remove_passenger("Eve")