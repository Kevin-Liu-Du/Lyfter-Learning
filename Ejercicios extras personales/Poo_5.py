class Person():
    def __init__(self, name):
        self.name = name

class Cinema():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.people = []

    def enter_person(self, person):
        if len(self.people) < self.capacity:
            self.people.append(person)
            print(f"{person.name} has entered the cinema.")
        else:
            print("The cinema is full. Cannot enter.")

    def leave_person(self, person):
        if person in self.people:
            self.people.remove(person)
            print(f"{person.name} has left the cinema.")
        else:
            print(f"{person.name} is not in the cinema.")

    def show_people(self):
        print(f"People in {self.name}:")
        for person in self.people:
            print(person.name)


person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
cinema = Cinema("CineMax", 2)
cinema.enter_person(person1)
cinema.enter_person(person2)
cinema.enter_person(person3)
cinema.show_people()
cinema.leave_person(person3)

